---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.033.001.03"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Transparency Data", "auth.033.001.03 "], "heading_paragraph": "P649", "xml_first_paragraph": "P653", "xml_last_paragraph": "P673", "rendered_file_pages": [53]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.033.001.03

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P649; XML P653–P673; Word file pages 53–53.

**P650** Description

**P651** The following MessageInstance provides an example of a Transparency Non-Equity message submitted by Borsa Italiana S.P.A.

**P652** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.033.001.03">
	<FinInstrmRptgNonEqtyTrnsprncyDataRpt>
		<RptHdr>
			<RptgNtty>
				<MktIdCd>XMIL</MktIdCd>
			</RptgNtty>
			<RptgPrd>
				<Dt>2013-12-31</Dt>
			</RptgPrd>
		</RptHdr>
		<NonEqtyTrnsprncyData>
			<TechRcrdId>123ABC</TechRcrdId>
			<Id>AB1234567890</Id>
			<FinInstrmClssfctn>BOND</FinInstrmClssfctn>
			<Bd>
				<Tp>EUSB</Tp>
				<IssncDt>2013-12-20</IssncDt>
			</Bd>
		</NonEqtyTrnsprncyData>
	</FinInstrmRptgNonEqtyTrnsprncyDataRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.033.001.03 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.033.001.03 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.033.001.03/index.md) · [Detailed test evidence and errors](../../../../../../../evidence/archived/434313c645b0c562cbe661e8.md)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
