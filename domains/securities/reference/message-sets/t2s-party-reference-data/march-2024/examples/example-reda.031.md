---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
message_families: ["reda.031"]
related_message_ids: ["reda.031.001.01"]
source_locations: [{"source_id": "src-000368", "heading_path": ["Business Examples", "Party Deletion Request - reda.031.001"], "first_paragraph": "P396", "last_paragraph": "P421", "rendered_file_pages": [35]}]
issue_ids: []
limitations: ["Examples omit target namespace and full definition version; no exact-schema-validity claim."]
---

# Party Deletion Request - reda.031.001

[src-000368](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; direct-body P396–P421; Word file pages 35–35. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.

**P397** Description

**P398** This example message is sent in order to delete the Party BANKXXYYAAA:

**P399** Party ID: BANKXXYYAAA

**P400** Responsible Party ID: NCBAXXYYAAA

**P401** Message Instance

**P402–P421**

```xml
<Document>
	<PtyDeltnReq>
		<MsgHdr>
			<MsgId>SAMPLEPARTYDEL</MsgId>
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
	</PtyDeltnReq>
</Document>


```

## XML inspection

| Paragraphs | Well-formedness |
| --- | --- |
| P402–P421 | well-formed |


[Related exact supplied definition reda.031.001.01](../../../../messages/reda.031.001.01/index.md)
