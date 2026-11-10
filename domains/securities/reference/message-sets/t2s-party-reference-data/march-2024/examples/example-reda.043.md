---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
message_families: ["reda.043"]
related_message_ids: ["reda.043.001.02"]
source_locations: [{"source_id": "src-000368", "heading_path": ["Business Examples", "Party Audit Trail Report - reda.043.001"], "first_paragraph": "P688", "last_paragraph": "P732", "rendered_file_pages": [45, 46]}]
issue_ids: []
limitations: ["Examples omit target namespace and full definition version; no exact-schema-validity claim."]
---

# Party Audit Trail Report - reda.043.001

[src-000368](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; direct-body P688–P732; Word file pages 45–46. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.

**P689** Description

**P690** The PartyAuditTrailReport (reda.043) message represents the answer to the Party Audit Trail Query described in the chapter 7.8. In this case, the party with ID PAYBXXYYAAA and responsible party ID NCBAXXYYAAA had only one change performed by the user USER1 and approved by the user USER2 on 2017-08-17T17:59:00 regarding the change of the Postal Code from the value 54321 to the new value 12345. 

**P691** Message Instance

**P692–P731**

```xml
<Document>
	<PtyAudtTrlRpt>
		<MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizInstr>
				<MsgId>SAMPLEPTYATRQUE</MsgId>
			</OrgnlBizInstr>
		</MsgHdr>
		<RptOrErr>
			<PtyAudtTrlRpt>
				<PtyAudtTrlOrErr>
					<AudtTrl>
						<Rcrd>
							<Othr>
							<FldNm>PostalCode</FldNm>
							<OdFldVal>54321</OdFldVal>
							<NewFldVal>12345</NewFldVal>
							</Othr>
						</Rcrd>
						<OprTmStmp>2017-08-17T17:59:00</OprTmStmp>
						<InstgUsr>USER1</InstgUsr>
						<ApprvgUsr>USER2</ApprvgUsr>
					</AudtTrl>
				</PtyAudtTrlOrErr>
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
			</PtyAudtTrlRpt>
		</RptOrErr>
	</PtyAudtTrlRpt>
</Document>
```


## XML inspection

| Paragraphs | Well-formedness |
| --- | --- |
| P692–P731 | well-formed |


[Related exact supplied definition reda.043.001.02](../../../../messages/reda.043.001.02/index.md)
