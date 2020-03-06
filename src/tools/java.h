#ifndef JAVA_H
#define JAVA_H

#include "base/command.h"

namespace Java
{
    class Version : public Command
    {
        Q_OBJECT

    public:
        Version(QObject *parent = nullptr) : Command(parent) {}
        void run() override;
        const QString &version() const;

    private:
        QString resultVersion;
    };
}

#endif // JAVA_H
