---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
message_families: ["reda.017"]
related_message_ids: ["reda.017.001.02"]
source_locations: [{"source_id": "src-000368", "heading_path": ["Business Examples", "Party Report - reda.017.001"], "first_paragraph": "P539", "last_paragraph": "P585", "rendered_file_pages": [40, 41]}]
issue_ids: []
limitations: ["Examples omit target namespace and full definition version; no exact-schema-validity claim."]
---

# Party Report - reda.017.001

[src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; direct-body P539–P585; Word file pages 40–41. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.

**P540** Description

**P541** The PartyReport (reda.017) message can be used as answer for:

**P542** Party Reference Data Query;

**P543** Party List Query;

**P544** Restricted Party Query

**P545** performed using the Party Query message (reda.015). This example shows the answer to the Party List Query described in the chapter 7.5. The query returns only one Party: 

**P546** Party ID: BANKXXYYAAA

**P547** Responsible Party ID: NCBAXXYYAAA

**P548** Party name: SAMPLE PAYMENT BANK

**P549** Party short name: SAMPLE

**P550** Message Instance

**P551–P584**

```xml
<Document>
	<PtyRpt>
		<MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizQry>
				<MsgId>SAMPLEPTYLISQUE</MsgId>
			</OrgnlBizQry>
		</MsgHdr>
		<RptOrErr>
			<PtyRpt>
				<PtyId>
					<Id>
						<Id>
							<AnyBIC>BANKXXYYAAA</AnyBIC>
						</Id>
					</Id>
					<RspnsblPtyId>
						<Id>
							<AnyBIC>NCBAXXYYAAA</AnyBIC>
						</Id>
					</RspnsblPtyId>
				</PtyId>
				<PtyOrErr>
					<SysPty>
						<Nm>
							<Nm>SAMPLE PAYMENT BANK</Nm>
							<ShrtNm>SAMPLE</ShrtNm>
						</Nm>
					</SysPty>
				</PtyOrErr>
			</PtyRpt>
		</RptOrErr>
	</PtyRpt>
</Document>
```


## XML inspection

| Paragraphs | Well-formedness |
| --- | --- |
| P551–P584 | well-formed |


[Related exact supplied definition reda.017.001.02](../../../../messages/reda.017.001.02/index.md)
