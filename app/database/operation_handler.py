import logging
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.models import Article, Source
from app.schemas.response import ResponseMessage
from app.schemas.articles import Article as ArticleSchema


class DatabaseOperationHandler:
    def __init__(self, db: Session):
        self.db = db

    def save_article(self, article_data: list[ArticleSchema]):
        try:
            logging.info("Starting to save articles to the database...")

            for article in article_data:
                source_id = None
                logging.info(f"Processing article: {article.title}")

                if article.source.id:
                    logging.info(
                        f"Checking for existing source with ID: {article.source.id}"
                    )

                    result = self.db.execute(
                        select(Source).filter(Source.source_id == article.source.id)
                    )
                    source = result.scalars().first()

                    if source:
                        logging.info(f"Found existing source with ID: {source.id}")
                        source_id = source.id
                    else:
                        logging.info(
                            f"Source not found, creating new source: {article.source.name}"
                        )
                        source = Source(
                            source_id=article.source.id, name=article.source.name
                        )
                        self.db.add(source)
                        self.db.commit()
                        self.db.refresh(source)
                        source_id = source.id
                        logging.info(f"Created new source with ID: {source.id}")

                elif article.source.name:
                    logging.info(
                        f"Source ID not provided, creating new source: {article.source.name}"
                    )
                    source = Source(source_id=None, name=article.source.name)
                    self.db.add(source)
                    self.db.commit()
                    self.db.refresh(source)
                    source_id = source.id
                    logging.info(f"Created new source with ID: {source.id}")

                new_article = Article(
                    author=article.author,
                    description=article.description,
                    url=article.url,
                    url_to_image=article.urlToImage,
                    published_at=article.publishedAt,
                    content=article.content,
                    source_id=source_id,
                )

                self.db.add(new_article)
                self.db.commit()
                self.db.refresh(new_article)
                logging.info(f"Article saved: {new_article.url}")

            logging.info("All articles saved successfully.")
            return ResponseMessage(
                **{"status": True, "message": "Articles saved successfully."}
            )
        except Exception as e:
            self.db.rollback()
            logging.error(f"Error saving articles: {str(e)}", exc_info=True)
            return ResponseMessage(
                **{"status": False, "message": f"Error saving articles: {str(e)}"}
            )

    # def delete_data(self, data):
    #     result = self.db.execute(select(Article).all())
    #     for row in result:
    #         if row.id / 2 == 0:
    #             self.db.delete(row)
    #             self.db.commit()
