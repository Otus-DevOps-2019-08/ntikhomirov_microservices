FROM alpine:latest

ENV APP_HOME /app
ENV POST_SERVICE_HOST post
ENV POST_SERVICE_PORT 5000
ENV COMMENT_SERVICE_HOST comment
ENV COMMENT_SERVICE_PORT 9292

WORKDIR $APP_HOME
ADD Gemfile* $APP_HOME/
RUN apk add --no-cache --virtual .build-deps build-base \
    && apk add ruby-full ruby-dev gcc libffi-dev make\
    && gem install puma -v '3.12.0' \
    && gem install bundler -v '1.17.2' \
    && gem install bson_ext -v '1.12.5' \
    && gem install thrift -v '0.9.3.0' \
    && apk del .build-deps

RUN bundle install
ADD . $APP_HOME

RUN rm -rf /var/cache/apk/*

CMD ["puma"]
