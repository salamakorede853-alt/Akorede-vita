#include <QApplication>
#include <QLabel>
#include <QMainWindow>
#include <QVBoxLayout>
#include <QWidget>

#include "akorede_vita/engine_status.h"

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);

    QMainWindow window;
    window.setWindowTitle("AKOREDE VITA");
    window.resize(1100, 720);

    auto* page = new QWidget(&window);
    auto* layout = new QVBoxLayout(page);

    auto* title = new QLabel("AKOREDE VITA", page);
    QFont titleFont = title->font();
    titleFont.setPointSize(24);
    titleFont.setBold(true);
    title->setFont(titleFont);

    auto* subtitle = new QLabel(
        "Windows application foundation • Emulator core not connected",
        page
    );
    auto* status = new QLabel(
        QString::fromUtf8(av_engine_status_message()),
        page
    );

    layout->addWidget(title);
    layout->addWidget(subtitle);
    layout->addWidget(status);
    layout->addStretch();

    window.setCentralWidget(page);
    window.show();

    return app.exec();
}
