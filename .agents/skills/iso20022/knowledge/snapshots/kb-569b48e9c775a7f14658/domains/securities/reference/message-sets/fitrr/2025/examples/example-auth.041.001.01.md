---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.041.001.01"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Transparency Data", "auth.041.001.01 "], "heading_paragraph": "P674", "xml_first_paragraph": "P678", "xml_last_paragraph": "P711", "rendered_file_pages": [54]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.041.001.01

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P674; XML P678–P711; Word file pages 54–54.

**P675** Description

**P676** The following MessageInstance provides an example of a Transparency Non-Equity trading activity message submitted by the Athens Stock Exchange.

**P677** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.041.001.01">
	<FinInstrmRptgNonEqtyTradgActvtyRpt>
		<RptHdr>
			<RptgNtty>
				<MktIdCd>ASEX</MktIdCd>
			</RptgNtty>
			<RptgPrd>
				<Dt>2013-12-31</Dt>
			</RptgPrd>
		</RptHdr>
		<NonEqtyTrnsprncyData>
			<TechRcrdId>123ABC</TechRcrdId>
			<Id>AB1234567890</Id>
			<Sspnsn>false</Sspnsn>
			<NbTxs>100</NbTxs>
			<AggtdQttvData>
				<NbOfTxs>40</NbOfTxs>
				<TtlNtnlAmt>1000</TtlNtnlAmt>
				<Rg>
					<FrQty>0</FrQty>
					<ToQty>100000</ToQty>
				</Rg>
			</AggtdQttvData>
			<AggtdQttvData>
				<NbOfTxs>60</NbOfTxs>
				<TtlNtnlAmt>1000</TtlNtnlAmt>
				<Rg>
					<FrQty>100000</FrQty>
					<ToQty>200000</ToQty>
				</Rg>
			</AggtdQttvData>
		</NonEqtyTrnsprncyData>
	</FinInstrmRptgNonEqtyTradgActvtyRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.041.001.01 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.041.001.01 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.041.001.01/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
