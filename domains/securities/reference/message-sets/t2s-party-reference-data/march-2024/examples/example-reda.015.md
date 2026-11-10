---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
message_families: ["reda.015"]
related_message_ids: ["reda.015.001.01"]
source_locations: [{"source_id": "src-000368", "heading_path": ["Business Examples", "Party Query - reda.015.001"], "first_paragraph": "P511", "last_paragraph": "P538", "rendered_file_pages": [39]}]
issue_ids: []
limitations: ["Examples omit target namespace and full definition version; no exact-schema-validity claim."]
---

# Party Query - reda.015.001

[src-000368](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; direct-body P511–P538; Word file pages 39–39. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.

**P512** Description

**P513** The PartyQuery (reda.015) message can be used to perform the following queries:

**P514** Party Reference Data Query;

**P515** Party List Query;

**P516** Restricted Party Query. 

**P517** In this example the NCB NCBAXXYYAAA performs a Party List Query, used to query all the party under the NCB data scope.

**P518** Message Instance

**P519–P538**

```xml
<Document>
	<PtyQry>
		<MsgHdr>
			<MsgId>SAMPLEPTYLISQUE</MsgId>
			<ReqTp>
				<Prtry>
					<Id>PYLI</Id>
				</Prtry>
			</ReqTp>
		</MsgHdr>
		<SchCrit>
			<RspnsblPtyId>
				<Id>
					<AnyBIC>NCBAXXYYAAA</AnyBIC>
				</Id>
			</RspnsblPtyId>
		</SchCrit>
	</PtyQry>
</Document>


```

## XML inspection

| Paragraphs | Well-formedness |
| --- | --- |
| P519–P538 | well-formed |


[Related exact supplied definition reda.015.001.01](../../../../messages/reda.015.001.01/index.md)
