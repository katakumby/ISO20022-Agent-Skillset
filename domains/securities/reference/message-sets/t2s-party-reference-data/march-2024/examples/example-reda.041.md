---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
message_families: ["reda.041"]
related_message_ids: ["reda.041.001.02"]
source_locations: [{"source_id": "src-000368", "heading_path": ["Business Examples", "Party Activity Advice - reda.041.001"], "first_paragraph": "P586", "last_paragraph": "P659", "rendered_file_pages": [42, 43]}]
issue_ids: ["issue-000046"]
limitations: ["Examples omit target namespace and full definition version; no exact-schema-validity claim."]
---

# Party Activity Advice - reda.041.001

[src-000368](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; direct-body P586–P659; Word file pages 42–43. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.

**P587** Description

**P588** The PartyActivityAdvice (reda.041) message provides information on changes occurred for party reference data during the business day. In this example, it shows two changes occurred on 2017-08-23 to the party PAYBXXYYAAA regarding the Party Long Name and its validity:

**P589** System date: 2017-08-23

**P590** First change:

**P591** Field changed: PartyName.ValidFrom

**P592** Party ID: BANKXXYYAAA

**P593** Responsible Party ID: NCBAXXYYAAA

**P594** Old Filed Value: 2008-07-01

**P595** New Field Value: 2017-08-23

**P596** Timestamp of the Update performed: 2017-08-23T15:10:10

**P597** Second change:

**P598** Field changed: PartyName.LongName

**P599** Party ID: BANKXXYYAAA

**P600** Responsible Party ID: NCBAXXYYAAA

**P601** Old Filed Value: SAMPLE NAME

**P602** New Field Value: NEW SAMPLE NAME

**P603** Timestamp of the Update performed: 2017-08-23T16:30:10

**P604** Message Instance

**P605–P659**

```xml
<Document>
	<PtyActvtyAdvc>
		<MsgHdr>
			<MsgId>SAMPLEPTYSTA</MsgId>
		</MsgHdr>
		<PtyActvty>
			<SysDt>2017-08-23</SysDt>
			<Chng>
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
				<Rcrd>
					<Othr>
						<FldNm>PartyName.ValidFrom</FldNm>
						<OdFldVal>2008-07-01</OdFldVal>
						<NewFldVal>2017-08-23</NewFldVal>						
					</Othr>					
				</Rcrd>				
				<OprTmStmp>2017-08-23T15:10:10</OprTmStmp>
			</Chng>
			<Chng>
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
				<Rcrd>
					<Othr>
						<FldNm>PartyName.LongName</FldNm>
						<OdFldVal>SAMPLE NAME</OdFldVal>
						<NewFldVal>NEW SAMPLE NAME</NewFldVal>
					</Othr>
				</Rcrd>
				<OprTmStmp>2017-08-23T16:30:10</OprTmStmp>
			</Chng>
		</PtyActvty>
	</PtyActvtyAdvc>
</Document>


```

## Literal source inconsistency

P588 and XML P616/P638 identify PAYBXXYYAAA, while P592/P599 list BANKXXYYAAA for the same activity-advice changes. Both values are preserved under issue-000046; no identity equivalence is inferred.

## XML inspection

| Paragraphs | Well-formedness |
| --- | --- |
| P605–P659 | well-formed |


[Related exact supplied definition reda.041.001.02](../../../../messages/reda.041.001.02/index.md)
