"""  
queryset - запросы в базу данных
по умолчанию запросы отправляются через переменную objects
objects - Manager, который содержит в себе все методы для общения с БД

Model.objects.all() - SELECT * FROM model
SELECT * FROM model LIMIT 2 - Model.objects.all()[:2]
SELECT * FROM model WHERE status='closed' - Model.objects.filter(status='closed)
SELECT * FROM model WHERE title LIKE/ILIKE 'название' - Publication.objects.filter(title__icontains='название')
Publication.objects.get(id=1) - SELECT * FROM publication WHERE id=1

Publication.objects.create(title='название1', image=None, status='open', user=u1)
INSERT INTO publication (title, image, status, user) VALUES (...)

Publication.objects.filter(status='closed').update(status='open')
UPDATE publication SET status='open' WHERE status='closed'

Publication.objects.get(title='название1').delete()
DELETE FROM publication WHERE title='название1'

"""