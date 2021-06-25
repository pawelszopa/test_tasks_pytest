# Pytest

`pytest [options] [file_or_dir] [file_or_dir] [...]`

## options

- `-k` Expression -  only run tests which match the given substring expression. 
    ```pytest -k "test_method or other``` - można dowolny warunek logiczny np. przy zamówieniu -k order and...
  
- `-m` Expression - tylko te które mają markery nałożone.
only run tests matching given mark expression. For example: -m 'mark1 and not mark2'.
  
- `-x` Expression - exit instantly on first error or faild test. - Failuje przy pierwszym teście, który failuje
- `--maxfail=num` - exit after first num failures or errors. Ile faili chcemy zobaczyć
- `--lf` - odpala testy, które się sfailowały w poprzednim wywaleniu
- `--ff` - odpala wszystkie testy, ale pierwsze które zfailowały
- `-v`- verbouse, zwiększa ilość informacji vs `-q` (quite)
- `-l` - pokazuje wartości zmiennych w danym test case (jak coś zfailuje to zobaczymy jakie zmienne były brane w nim)
- `-tb` - traceback
- `-collect-only` - pokazuje tylko które testy będą uruchomione
- `durations` - czas trania maksymalny


` 1954  python -m site
 1955  pytest
 1956  python -m site
 1957  pytest -k "asdict" --collect-only
 1958  pytest -k "asdict or defaults" --collect-only
 1959  pytest -m smoke
 1960* 
 1961  pytest -m smoke
 1962  pytest -m "smoke and not get"
 1963  pytest -m "smoke and not get" --collect-only
 1964  pytest -m "smoke" --collect-only
 1965  pytest -m "smoke and not get"
 1966  pytest -m "smoke"
 1967  pytest -x
 1968  pytest --maxfail=2
 1969  pytest --lf
 1970  pytest --ff
 1971  pytest --lf
 1972  pytest -v
 1973  pytest -q
 1974  pytest -l
 1975  pytest -tb=no
 1976  pytest -durations
 1977  =3
 1978  pytest -durations=3
 1979  pytest -l
 1980  pytest --durations=3`





- pliki inicializujące do pytesta:

Przeszukiwanie scopów

RHS - right hand side assigment, lokalny sprawdza, enclosing, global, b.. LHS - left hand side assigment, po lewej mamy
zmienną, po prawej przypisanie wartości, jak nie znajduje takiej zmiennej to ją tworzy i nie przeszukuje dalej, dlatego
podajemy global, żeby znalazło zmienną w globalu

Mongo:

...

standard out - standardowe wyjście, defaultowe np. Pip freeze - i wyświetla standardowy out i przykład przekierowania
streamu: pip freeze > requirements.txt

standardowy error - standardowo gdzie się mają zapisywać błędy

I przy subprocessach wyrzuca się gdzieś te rzeczy, bo subproces też ma swój terminal i nie możemy tego tak zobaczyć

** os.devnull - nigdzie się nie będzie zapisywał, tylko go zobaczymy

** fasada a adapter - fasada robi klika adapterów do kilku, adapter jeden (np potrzebujemy tylko kilku funkcjonalnosci
do bazy, anie wszystkich i chcemy to uproscic)

** markery w pytest - jakieś skipy, tworzy się je, jako dekoratory do unittestów i używa się ich w CLI pytesta


`if __name__ == '__main__':
    task_cli()`

kontext uruchomienia modułu


smoke testy - sprawdzają kluczowe elementy aplikacji, które działają

