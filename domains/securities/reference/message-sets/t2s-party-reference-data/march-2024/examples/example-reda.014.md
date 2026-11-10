---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
message_families: ["reda.014"]
related_message_ids: ["reda.014.001.02"]
source_locations: [{"source_id": "src-000368", "heading_path": ["Business Examples", "Party Creation Request - reda.014.001"], "first_paragraph": "P301", "last_paragraph": "P355", "rendered_file_pages": [32, 33]}]
issue_ids: []
limitations: ["Examples omit target namespace and full definition version; no exact-schema-validity claim."]
---

# Party Creation Request - reda.014.001

[src-000368](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; direct-body P301–P355; Word file pages 32–33. These are source-authored examples. Headings omit the final definition version and XML omits a namespace; no exact-version schema-validity claim is made.

**P302** Description

**P303** The instructing Party wants to create a new Payment Bank with the following information:

**P304** Party code: BANKXXYYAAA

**P305** Party code Valid From: 2017-09-01

**P306** Street name: Via Nazionale

**P307** Postal code: 00184

**P308** Town name: Rome

**P309** Country: IT

**P310** Party address valid from: 2011-01-01

**P311** Party Opening Date: 2017-08-23

**P312** Party Type: PMBK

**P313** Party Tech. Address: Example_PTA

**P314** Party Name valid from: 2008-07-01

**P315** Party Name: SAMPLE PAYMENT BANK

**P316** Party short Name: SAMPLE

**P317** Message Instance

**P318–P355**

```xml
<Document>
	<PtyCreReq>
		<MsgHdr>
			<MsgId>SAMPLEPARTYCRE</MsgId>
		</MsgHdr>
		<Pty>
			<PtyId>
				<Id>
					<Id>
						<AnyBIC>BANKXXYYAAA</AnyBIC>
					</Id>
				</Id>
				<VldFr>2017-09-01</VldFr>
			</PtyId>
			<Adr>
				<StrtNm>Via Nazionale</StrtNm>
				<BldgNb>1</BldgNb>
				<PstCd>00184</PstCd>
				<TwnNm>Rome</TwnNm>
				<Ctry>IT</Ctry>
				<VldFr>2011-01-01</VldFr>
			</Adr>
			<OpngDt>2017-08-23</OpngDt>
			<Tp>
				<Cd>PMBK</Cd>
			</Tp>
			<TechAdr>
				<TechAdr>Example_PTA</TechAdr>
			</TechAdr>
			<Nm>
				<VldFr>2008-07-01</VldFr>
				<Nm>SAMPLE PAYMENT BANK</Nm>
				<ShrtNm>SAMPLE</ShrtNm>
			</Nm>
		</Pty>
	</PtyCreReq>
</Document>


```

## XML inspection

| Paragraphs | Well-formedness |
| --- | --- |
| P318–P355 | well-formed |


[Related exact supplied definition reda.014.001.02](../../../../messages/reda.014.001.02/index.md)
