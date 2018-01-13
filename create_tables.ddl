-- dodałem ID w niektórych relacjach (chyba tylko w tych pośredniczących z ManyToMany),
-- może lepiej to usunąć przed wysłaniem, bo to w sumie chyba był błąd

CREATE TABLE Student (
  ID        SERIAL       NOT NULL,
  Imie      VARCHAR(255) NOT NULL,
  Nazwisko  VARCHAR(255) NOT NULL,
  Login     VARCHAR(30)  NOT NULL UNIQUE,
  Haslo     VARCHAR(255) NOT NULL,
  NrIndeksu VARCHAR(9)   NOT NULL UNIQUE,
  PRIMARY KEY (ID)
);
CREATE TABLE NauczycielAkademicki (
  ID                 SERIAL       NOT NULL,
  Imie               VARCHAR(255) NOT NULL,
  Nazwisko           VARCHAR(255) NOT NULL,
  Login              VARCHAR(30)  NOT NULL UNIQUE,
  Haslo              VARCHAR(255) NOT NULL,
  LiczbaGodzin       INT4         NOT NULL,
  Pensum             INT4         NOT NULL,
  JestPelnomocnikiem BOOL         NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE Kurs (
  ID               SERIAL       NOT NULL,
  WartoscGodzinowa INT4         NOT NULL,
  ECTS             INT4         NOT NULL,
  NazwaKursu       VARCHAR(255) NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE GrupaZajeciowa (
  ID                SERIAL NOT NULL,
  KursID            INT4   NOT NULL,
  StudentID         INT4   NOT NULL,
  RodzajGrupy       INT4   NOT NULL,
  CzyUruchomiona    BOOL   NOT NULL,
  LiczbaMiejsc      INT4   NOT NULL,
  LiczbaUczestnikow INT4   NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE Opinia (
  ID                     SERIAL        NOT NULL,
  GrupaZajeciowaID       INT4          NOT NULL,
  NauczycielAkademickiID INT4          NOT NULL,
  Tresc                  VARCHAR(2500) NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE WniosekOUruchomienieGrupyZajeciowej (
  ID                SERIAL NOT NULL,
  StudentID         INT4   NOT NULL,
  ZgodaPelnomocnika BOOL,
  StatusWniosku     INT4,
  NrWniosku         INT4   NOT NULL,
  GrupaZajeciowaID  INT4   NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE Termin (
  ID               SERIAL      NOT NULL,
  GrupaZajeciowaID INT4,
  Dzien            INT4,
  Godzina          VARCHAR(10),
  Sala             VARCHAR(10) NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE DzienTygodnia (
  ID    SERIAL      NOT NULL,
  nazwa VARCHAR(32) NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE RodzajGrupy (
  ID    SERIAL      NOT NULL,
  nazwa VARCHAR(32) NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE StatusWniosku (
  ID    SERIAL      NOT NULL,
  nazwa VARCHAR(32) NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE NauczycielAkademicki_Kurs (
  ID    SERIAL      NOT NULL,
  NauczycielAkademickiID INT4 NOT NULL,
  KursID                 INT4 NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE NauczycielAkademicki_Kurs2 (
  ID    SERIAL      NOT NULL,
  NauczycielAkademickiID INT4 NOT NULL,
  KursID                 INT4 NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE Kurs_Kurs (
  ID    SERIAL      NOT NULL,
  KursID  INT4 NOT NULL,
  KursID2 INT4 NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE Student_GrupaZajeciowa (
  ID    SERIAL      NOT NULL,
  StudentID        INT4 NOT NULL,
  GrupaZajeciowaID INT4 NOT NULL,
  PRIMARY KEY (ID)
);
CREATE TABLE GrupaZajeciowa_NauczycielAkademicki (
  ID    SERIAL      NOT NULL,
  GrupaZajeciowaID       INT4 NOT NULL,
  NauczycielAkademickiID INT4 NOT NULL,
  PRIMARY KEY (ID)
);
ALTER TABLE NauczycielAkademicki_Kurs
  ADD CONSTRAINT opiekujeSie FOREIGN KEY (NauczycielAkademickiID) REFERENCES NauczycielAkademicki (ID);
ALTER TABLE NauczycielAkademicki_Kurs
  ADD CONSTRAINT opiekujeSie2 FOREIGN KEY (KursID) REFERENCES Kurs (ID);
ALTER TABLE NauczycielAkademicki_Kurs2
  ADD CONSTRAINT mozeProwadzic FOREIGN KEY (NauczycielAkademickiID) REFERENCES NauczycielAkademicki (ID);
ALTER TABLE NauczycielAkademicki_Kurs2
  ADD CONSTRAINT mozeProwadzic2 FOREIGN KEY (KursID) REFERENCES Kurs (ID);
ALTER TABLE Kurs_Kurs
  ADD CONSTRAINT jestZamiennikiem FOREIGN KEY (KursID) REFERENCES Kurs (ID);
ALTER TABLE Kurs_Kurs
  ADD CONSTRAINT jestZamiennikiem2 FOREIGN KEY (KursID2) REFERENCES Kurs (ID);
ALTER TABLE GrupaZajeciowa
  ADD CONSTRAINT organizuje FOREIGN KEY (StudentID) REFERENCES Student (ID);
ALTER TABLE Student_GrupaZajeciowa
  ADD CONSTRAINT uczestniczy FOREIGN KEY (StudentID) REFERENCES Student (ID);
ALTER TABLE Student_GrupaZajeciowa
  ADD CONSTRAINT uczestniczy2 FOREIGN KEY (GrupaZajeciowaID) REFERENCES GrupaZajeciowa (ID);
ALTER TABLE GrupaZajeciowa
  ADD CONSTRAINT obejmuje FOREIGN KEY (KursID) REFERENCES Kurs (ID);
ALTER TABLE GrupaZajeciowa_NauczycielAkademicki
  ADD CONSTRAINT prowadzi FOREIGN KEY (GrupaZajeciowaID) REFERENCES GrupaZajeciowa (ID);
ALTER TABLE GrupaZajeciowa_NauczycielAkademicki
  ADD CONSTRAINT prowadzi2 FOREIGN KEY (NauczycielAkademickiID) REFERENCES NauczycielAkademicki (ID);
ALTER TABLE Opinia
  ADD CONSTRAINT wystawia FOREIGN KEY (NauczycielAkademickiID) REFERENCES NauczycielAkademicki (ID);
ALTER TABLE Opinia
  ADD CONSTRAINT tyczySie FOREIGN KEY (GrupaZajeciowaID) REFERENCES GrupaZajeciowa (ID);
ALTER TABLE WniosekOUruchomienieGrupyZajeciowej
  ADD CONSTRAINT tworzy FOREIGN KEY (StudentID) REFERENCES Student (ID);
ALTER TABLE Termin
  ADD CONSTRAINT odbywaSieW FOREIGN KEY (GrupaZajeciowaID) REFERENCES GrupaZajeciowa (ID);
ALTER TABLE Termin
  ADD CONSTRAINT FKTermin622761 FOREIGN KEY (Dzien) REFERENCES DzienTygodnia (ID);
ALTER TABLE WniosekOUruchomienieGrupyZajeciowej
  ADD CONSTRAINT FKWniosekOUr738413 FOREIGN KEY (StatusWniosku) REFERENCES StatusWniosku (ID);
ALTER TABLE GrupaZajeciowa
  ADD CONSTRAINT FKGrupaZajec946553 FOREIGN KEY (RodzajGrupy) REFERENCES RodzajGrupy (ID);
ALTER TABLE WniosekOUruchomienieGrupyZajeciowej
  ADD CONSTRAINT FKWniosekOUr464836 FOREIGN KEY (GrupaZajeciowaID) REFERENCES GrupaZajeciowa (ID);

