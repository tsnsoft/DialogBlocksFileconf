# DialogBlocksFileсonf
Пример консольной программы работы с файлом настроек на C++ с использованием wxWidgets и DialogBlocks в Visual Studio 2022

![srcreenshot](screenshot1.png)

![srcreenshot](screenshot2.png)

```
#include <wx/wx.h>
#include <wx/fileconf.h>
#include <wx/stdpaths.h>

int main(int argc, char** argv) {

	wxApp myApp; // Создать объект wxApp-приложения

	wxInitializer initializer(argc, argv); // Инициализировать приложение
	if (!initializer.IsOk()) { // Если инициализация не удалась
		wxPuts(wxT("Failed to initialize the application!")); // Вывести сообщение
		return -1; // Завершить программу с кодом -1
	}

	setlocale(LC_ALL, "ru_RU.UTF-8"); // Установить русскую локаль для Linux
	wxLocale m_locale; // Создать объект локали для wxWidgets
	m_locale.Init(wxLANGUAGE_RUSSIAN, wxLOCALE_DONT_LOAD_DEFAULT); // Установить локаль для wxWidgets

#ifdef __WXMSW__ // Определение для Windows
	_setmode(_fileno(stdout), _O_U16TEXT); // Установить Юникод для вывода в консоли Windows
	_setmode(_fileno(stdin), _O_U16TEXT); // Установить Юникод для ввода в консоли Windows
	_setmode(_fileno(stderr), _O_U16TEXT); // Установить Юникод для вывода ошибок в консоли Windows
#endif

	wxPuts(wxT("Работа с файлом настроек")); // Вывести строку

	wxFileConfig* m_fileconfig; // Объявление указателя на объект конфигурации

	// Создать имя для файла конфигурации приложения
	wxFileName fn = wxFileName(wxPathOnly(wxStandardPaths::Get().GetExecutablePath()), myApp.GetAppName(),
		wxT("ini"));

	// Создать объект конфигурации приложения
	m_fileconfig = new wxFileConfig(wxEmptyString, wxEmptyString, fn.GetFullPath(), wxEmptyString,
		wxCONFIG_USE_LOCAL_FILE | wxCONFIG_USE_NO_ESCAPE_CHARACTERS);

	wxConfigBase::Set(m_fileconfig); // Установить объект конфигурации приложения

	wxConfigBase* conf = wxConfigBase::Get(false); // Получить объект конфигурации приложения

	if (!conf) myApp.Exit(); // Если объект конфигурации приложения не создан, то завершить приложение

	conf -> SetPath(wxT("/settings")); // Установить путь в конфигурации
	conf->Write(wxT("language_ru"), wxT("русский")); // Записать значение в конфигурацию
	
	conf->SetPath(wxT("/settings_add")); // Установить путь в конфигурации
	conf->Write(wxT("language_en"), wxT("английский")); // Записать значение в конфигурацию
	conf->Write(wxT("language_de"), wxT("немецкий")); // Записать значение в конфигурацию

	wxPuts(conf->Read(wxT("language_de"), wxT("de ?"))); // Прочитать значение из конфигурации
	wxPuts(conf->Read(wxT("language_en"), wxT("en ?"))); // Прочитать значение из конфигурации

	conf->SetPath(wxT("/settings")); // Установить путь в конфигурации
	wxPuts(conf->Read(wxT("language_ru"), wxT("ru ?"))); // Прочитать значение из конфигурации

	if (m_fileconfig) { // Если объект конфигурации приложения создан
		m_fileconfig->Flush(); // Сохранить настройки в файл
		delete m_fileconfig; // Удалить объект конфигурации приложения
		m_fileconfig = NULL; // Установить указатель на объект конфигурации приложения в NULL
	}
	wxConfigBase::Set(NULL); // Установить объект конфигурации приложения в NULL

#ifdef __WXMSW__ // Определение для Windows
	system("pause"); // Приостановить выполнение программы
#else // Определение для Linux
	system("read -p \"Нажмите Enter для продолжения...\"  var"); // Приостановить выполнение программы
#endif

	myApp.Exit(); // Завершить работу приложения
}
```

## Настройки DialogBlocks:

**WXWIN:** D:\Development\CPP\wxWidgetsDBls

**DBPROJECTS:** D:\Projects\DialogBlocksProjects

**MSBUILDDIR:** C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin

**MSVCDIR:** C:\Program Files\Microsoft Visual Studio\2022\Community

**PLATFORMSDK:** C:\Program Files (x86)\Windows Kits\10

**VC++ version:** 17 <<-- Microsoft Visual Studio Community 2022 (64-разрядная версия) - Версия 17.8.2

**VC++ tools version:** 14.38.33130 <<-- C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.38.33130

**Full Platform SDK version**: 10.0.22621.0 <<-- C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0

**Message encoding:** cp866

*Чтобы компилировался проект без BOM в UTF-8 в конфигурации сборки укажите:*

**Extra compile flags:** %AUTO% /utf-8

*Чтобы компилировался проект в режиме консоли в конфигурации каждой сборки также укажите:*

**GUI mode:** Console

## Ссылки:

http://www.anthemion.co.uk/dialogblocks/DialogBlocks-5.18-beta3-Setup.exe

http://www.anthemion.co.uk/dialogblocks/

https://www.wxwidgets.org/

https://visualstudio.microsoft.com/ru/vs/community/
