# Ek Ders

## Dosyaları görüntüleme

Dosyaların oluşturma zamanın görüntüleyeceğiz, ancak `Path()` Unix zamanı olarak döndürdüğünden bunu unix ctime veya istediğiniz bir formata dönüştürmek
için `get_time` filteresini yazalım. `microblog/application.py` dosyasını açın, başa `import time` ekleyin, `create_app()` fonksiyonunun en altına aşağıdaki filtereyi yazın:

```
    @app.template_filter()
    def get_time(timestamp):
        return time.ctime(timestamp)
```

`microblog/views/files.py` dosyasının başına `from pathlib import Path` ekleyin, ve `index()` fonksiyonuna `return` den önce:

`user_files_path = Path(current_user.upload_dir)`

ekleyin ve bunu template gönderin:

`return render_template('files/index.html', title=title, form=form, user_files_path=user_files_path)`

`microblog/microblog/views/files/index.html` dosyasına `endblock`dan önce aşağıdaki satırları ekleyin:

```
  <table class="table table-condensed">
  <thead><th>Dosya Adı</th><th>Boyut (Kb)</th><th>Yükleme Tarihi</th><th></th></thead>

  {% for file_path in user_files_path.glob('*') %}
    <tr>
      <td>{{ file_path.relative_to(current_user.upload_dir) }}</td>
      <td>{{ file_path.stat().st_size}}</td>
      <td>{{ file_path.stat().st_mtime | get_time }}</td>
      <td><a href="#"><span class="glyphicon glyphicon-download-alt"></span></a></td>
    </tr>
  {% endfor %}

  </table>
```

İndirme ve silme linkini daha sonra yazacağız.

Şimdi tarayıcıda şu şekilde görünecektir. 

![Dosya Listeleme](docs/img/dosya_listesi.png)
