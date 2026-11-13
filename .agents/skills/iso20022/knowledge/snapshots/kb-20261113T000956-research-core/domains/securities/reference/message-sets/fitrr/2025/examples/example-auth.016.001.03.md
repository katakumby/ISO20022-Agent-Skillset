---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.016.001.03"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Transaction Reporting", "auth.016.001.03 "], "heading_paragraph": "P780", "xml_first_paragraph": "P784", "xml_last_paragraph": "P836", "rendered_file_pages": [56, 57, 58]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.016.001.03

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P780; XML P784–P836; Word file pages 56–58.

**P781** Description

**P782** The following MessageInstance provides an example of a Transaction Report Message that is being executed and reported by the entity with LEI 00000000000000000000. The transaction was executed in the instrument identified by AB1234567890 and took place on the venue XDUB.

**P783** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.016.001.03">
	<FinInstrmRptgTxRpt>
		<Tx>
			<New>
				<TxId>T123456</TxId>
				<ExctgPty>00000000000000000000</ExctgPty>
				<InvstmtPtyInd>true</InvstmtPtyInd>
				<SubmitgPty>00000000000000000000</SubmitgPty>
				<Buyr>
					<AcctOwnr>
						<Id>
							<LEI>11111111111111111111</LEI>
						</Id>
					</AcctOwnr>
				</Buyr>
				<Sellr>
					<AcctOwnr>
						<Id>
							<LEI>22222222222222222222</LEI>
						</Id>
					</AcctOwnr>
				</Sellr>
				<OrdrTrnsmssn>
					<TrnsmssnInd>true</TrnsmssnInd>
				</OrdrTrnsmssn>
				<Tx>
					<TradDt>2018-12-17T09:30:47Z</TradDt>
					<TradgCpcty>MTCH</TradgCpcty>
					<Qty>
						<Unit>100</Unit>
					</Qty>
					<Pric>
						<Pric>
							<MntryVal>
								<Amt Ccy="EUR">13.5</Amt>
							</MntryVal>
						</Pric>
					</Pric>
					<TradVn>XDUB</TradVn>
				</Tx>
				<FinInstrm>
					<Id>AB1234567890</Id>
				</FinInstrm>
				<ExctgPrsn>
					<Algo>A123456</Algo>
				</ExctgPrsn>
				<AddtlAttrbts>
					<SctiesFincgTxInd>true</SctiesFincgTxInd>
				</AddtlAttrbts>
			</New>
		</Tx>
	</FinInstrmRptgTxRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.016.001.03 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.016.001.03 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.016.001.03/index.md) · [Detailed test evidence and errors](../../../../../../../evidence/archived/434313c645b0c562cbe661e8.md)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
