from scripts.process_urls import process_url


def test_filename_entity_0():
    assert process_url("dockerfile") == "dockerfile"


def test_filename_entity_1():
    assert process_url("ngModel.js") == "ngModel.js"


def test_filename_entity_2():
    assert process_url("MyService.service.js") == "MyService.service.js"


def test_filename_entity_3():
    assert (
        process_url(".pipelines/pipeline.user.windows.yml")
        == ".pipelines/pipeline.user.windows.yml"
    )


def test_filename_entity_4():
    assert process_url("/etc/docker/daemon.json") == "/etc/docker/daemon.json"


def test_filename_entity_5():
    assert (
        process_url("moby/daemon/logger/awslogs/cloudwatchlogs.go")
        == "moby/daemon/logger/awslogs/cloudwatchlogs.go"
    )


def test_filename_entity_6():
    assert (
        process_url("https://github.com/angular/angular.js/blob/master/src/minErr.js")
        == "src/minErr.js"
    )


def test_filename_entity_7():
    assert (
        process_url(
            "https://github.com/opencontainers/runc/blob/7c219d814fc5f5574a7aab836fb2b89e3c5d2dfd/libcontainer/init_linux.go#L380"
        )
        == "libcontainer/init_linux.go"
    )


def test_filename_entity_8():
    assert (
        process_url(
            "https://github.com/docker/cli/blob/b0343d9104a1794c3252fa45b985710d6b6afc05/cli/command/container/run.go#L151-L163"
        )
        == "cli/command/container/run.go"
    )


def test_branchname_entity_0():
    assert process_url("1.6.0.rc-0") == "1.6.0.rc-0"


def test_branchname_entity_1():
    assert process_url("1.3") == "1.3"


def test_branchname_entity_2():
    assert process_url("feature/vue-3") == "feature/vue-3"


def test_branchname_entity_3():
    assert process_url("vue-next") == "vue-next"


def test_branchname_entity_4():
    assert (
        process_url("https://github.com/microsoft/PowerToys/tree/fixingSsigningDlls")
        == "fixingSsigningDlls"
    )


def test_branchname_entity_5():
    assert (
        process_url("https://github.com/vuejs/vue-next/tree/fix/missing-computed")
        == "fix/missing-computed"
    )


def test_issue_number_entity_0():
    assert process_url("#17117") == "#17117"


def test_issue_number_entity_1():
    assert (
        process_url("angular/code.angularjs.org#38") == "angular/code.angularjs.org#38"
    )


def test_issue_number_entity_2():
    assert process_url("https://github.com/angular/angular.js/issues/16916") == "#16916"
