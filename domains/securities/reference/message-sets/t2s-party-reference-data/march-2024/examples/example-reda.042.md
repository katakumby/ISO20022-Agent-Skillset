---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
message_families: ["reda.042"]
related_message_ids: ["reda.042.001.01"]
source_locations: [{"source_id": "src-000368", "heading_path": ["Business Examples", "Party Audit Trail Query - reda.042.001"], "first_paragraph": "P660", "last_paragraph": "P687", "rendered_file_pages": [44]}]
issue_ids: []
limitations: ["Examples omit target namespace and full definition version; no exact-schema-validity claim."]
---

# Party Audit Trail Query - reda.042.001

[src-000368](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; direct-body P660–P687; Word file pages 44–44. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.

**P661** Description

**P662** The PartyAuditTrailQuery (reda.042) is used to query all the audit trails regarding the Party with:

**P663** ID PAYBXXYYAAA

**P664** Responsible Party ID NCBAXXYYAAA

**P665** Message Instance

**P666–P687**

```xml
<Document>
	<PtyAudtTrlQry>
		<MsgHdr>
			<MsgId>SAMPLEPTYATRQUE</MsgId>
		</MsgHdr>
		<SchCrit>
			<PtyId>
				<Id>
					<Id>
						<AnyBIC>PAYBXXYYAAA</AnyBIC>
					</Id>
				</Id>
				<RspnsblPtyId>
					<Id>
						<AnyBIC>NCBAXXYYAAA</AnyBIC>
					</Id>
				</RspnsblPtyId>
			</PtyId>
		</SchCrit>
	</PtyAudtTrlQry>
</Document>


```

## XML inspection

| Paragraphs | Well-formedness |
| --- | --- |
| P666–P687 | well-formed |


[Related exact supplied definition reda.042.001.01](../../../../messages/reda.042.001.01/index.md)
