# Used in CI for nightly packaging

set -x
set -e

mvloc batch-apply $1 -m
mvloc package $1 -m

mv report.txt "packages/batch-apply-report-$1-machine.txt"
cp "output-$1/mod-appendix/metadata.xml" "packages/metadata-$1-machine.xml"

pushd "output-$1"
zip -r "../packages/xml_only-$1-machine.zip" *
popd
