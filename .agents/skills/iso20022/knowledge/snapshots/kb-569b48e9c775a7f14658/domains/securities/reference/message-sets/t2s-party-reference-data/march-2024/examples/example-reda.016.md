---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
message_families: ["reda.016"]
related_message_ids: ["reda.016.001.01"]
source_locations: [{"source_id": "src-000368", "heading_path": ["Business Examples", "Party Status Advice- reda.016.001"], "first_paragraph": "P422", "last_paragraph": "P510", "rendered_file_pages": [36, 37, 38]}]
issue_ids: []
limitations: ["Examples omit target namespace and full definition version; no exact-schema-validity claim."]
---

# Party Status Advice- reda.016.001

[src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; direct-body P422–P510; Word file pages 36–38. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.

**P423** Description

**P424** The following examples are referred to the status advice related to the Party deletion request of the chapter 7.3. in three different cases:

**P425** Deletion completed successfully;

**P426** Deletion queued;

**P427** Deletion rejected.

**P428** Party Status Advice- reda.016.001– Completed example

**P429** In this case the Party Deletion Request has been successfully executed.

**P430** Original Message ID: SAMPLEPARTYDEL

**P431** Party ID: BANKXXYYAAA

**P432** Responsible Party ID: NCBAXXYYAAA

**P433** Status. COMP

**P434** Message Instance

**P435–P459**

```xml
<Document>
	<PtyStsAdvc>
		<MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizInstr>
				<MsgId>SAMPLEPARTYDEL</MsgId>
			</OrgnlBizInstr>
		</MsgHdr>
		<PtySts>
			<Sts>COMP</Sts>
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
		</PtySts>
	</PtyStsAdvc>
</Document>
```

**P460** Party Status Advice- reda.016.001 – Queued example

**P461** This example describes the case in which the Party Deletion Request has been delayed. In case of e.g. a night-time cycle is running.  

**P462** Original Message ID: SAMPLEPARTYDEL

**P463** Status: QUED

**P464** Additional Information: REQUEST HAS BEEN QUEUED

**P465** Message Instance

**P466–P484**

```xml
<Document >
	<PtyStsAdvc>
		<MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizInstr>
				<MsgId>SAMPLEPARTYDEL</MsgId>
			</OrgnlBizInstr>
		</MsgHdr>
		<PtySts>
			<Sts>QUED</Sts>
			<StsRsn>
				<Rsn>
					<Prtry>QUED</Prtry>
				</Rsn>
				<AddtlInf>REQUEST HAS BEEN QUEUED</AddtlInf>
			</StsRsn>
		</PtySts>
	</PtyStsAdvc>
</Document>
```

**P485** Party Status Advice- reda.016.001 – Rejected example

**P486** In this example the Party Status Advice reports that the Party Deletion Request has been rejected, specifying the rejection reason.

**P487** Original Message ID: SAMPLEPARTYDEL

**P488** Status. REJT

**P489** Additional Information: ABCD000 PARTY DELETION REQUEST REJECTED

**P490** Message Instance

**P491–P510**

```xml
<Document>
	<PtyStsAdvc>
		<MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizInstr>
				<MsgId>SAMPLEPARTYDEL</MsgId>
			</OrgnlBizInstr>
		</MsgHdr>
		<PtySts>
			<Sts>REJT</Sts>
			<StsRsn>
				<Rsn>
					<Prtry>REJT</Prtry>
				</Rsn>
				<AddtlInf>ABCD000 PARTY DELETION REQUEST REJECTED</AddtlInf>
			</StsRsn>
		</PtySts>
	</PtyStsAdvc>
</Document>


```

## XML inspection

| Paragraphs | Well-formedness |
| --- | --- |
| P435–P459 | well-formed |
| P466–P484 | well-formed |
| P491–P510 | well-formed |


[Related exact supplied definition reda.016.001.01](../../../../messages/reda.016.001.01/index.md)
