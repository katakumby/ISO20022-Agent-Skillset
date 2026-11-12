---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
message_families: ["reda.022"]
related_message_ids: ["reda.022.001.02"]
source_locations: [{"source_id": "src-000368", "heading_path": ["Business Examples", "Party Modification Request - reda.022.001"], "first_paragraph": "P356", "last_paragraph": "P395", "rendered_file_pages": [34]}]
issue_ids: []
limitations: ["Examples omit target namespace and full definition version; no exact-schema-validity claim."]
---

# Party Modification Request - reda.022.001

[src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; direct-body P356–P395; Word file pages 34–34. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.

**P357** Description

**P358** In this example, the instructing party wants to update the Street name and the building number of the Party BANKXXYYAAA:

**P359** Party ID: BANKXXYYAAA

**P360** Responsible Party ID: NCBAXXYYAAA

**P361** New Street name: Largo Guido Carli

**P362** Building number: 01

**P363** Address Valid From: 2017-08-23

**P364** Message Instance

**P366–P395**

```xml
<Document>
	<PtyModReq>
		<MsgHdr>
			<MsgId>SAMPLEPARTYUPD</MsgId>
		</MsgHdr>
		<SysPtyId>
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
		</SysPtyId>
		<Mod>
			<ScpIndctn>UPDT</ScpIndctn>
			<ReqdMod>
				<PtyAdr>
					<StrtNm>Largo Guido Carli</StrtNm>
					<BldgNb>01</BldgNb>
					<VldFr>2017-08-23</VldFr>
				</PtyAdr>
			</ReqdMod>
		</Mod>
	</PtyModReq>
</Document>


```

## XML inspection

| Paragraphs | Well-formedness |
| --- | --- |
| P366–P395 | well-formed |


[Related exact supplied definition reda.022.001.02](../../../../messages/reda.022.001.02/index.md)
