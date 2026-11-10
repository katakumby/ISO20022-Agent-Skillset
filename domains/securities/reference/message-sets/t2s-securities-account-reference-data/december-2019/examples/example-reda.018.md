---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.018.001.01"]
source_locations: [{"source_id": "src-000371", "heading_path": ["Business Examples", "Securities Account Creation Request - reda.018.001.01"], "first_paragraph": "P329", "last_paragraph": "P372", "rendered_file_pages": [32, 33]}]
issue_ids: ["issue-000050"]
limitations: ["The original has no namespace. Schema-validation results refer only to the explicitly derived namespace-assigned copy; the literal source XML is unchanged."]
---

# Securities Account Creation Request - reda.018.001.01

[src-000371](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P329–P372; Word file pages 32–33. This is the literal source example. Original XML is retained without a namespace; schema testing below uses only an explicitly derived namespace assignment.

**P330** Description

**P331** The instructing Party wants to create a new securities account with the following information:

**P332** Account owner Parent BIC: CSDAXXYYAAA

**P333** Account owner Party BIC: CSDPXXYYAAA 

**P334** Security account identification: SECACCCSDPXXYYAAA

**P335** Account Type: CSDP

**P336** Opening date: 2019-01-01

**P337** Hold indicator: true

**P338** Negative position indicator: false

**P339** End investor flag: NONE

**P340** Pricing scheme: SACC

**P341** Message Instance

**P342–P372**

```xml
<Document>
<Document>
	<SctiesAcctCreReq>
		<MsgHdr>
			<MsgId>SAMPLECRESAC</MsgId>
		</MsgHdr>
		<SctiesAcct>
			<AcctOwnr>
				<Id>
					<Id>
						<AnyBIC>CSDPXXYYAAA</AnyBIC>
					</Id>
				</Id>
				<RspnsblPtyId>
					<Id>
						<AnyBIC>CSDAXXYYAAA</AnyBIC>
					</Id>
				</RspnsblPtyId>
			</AcctOwnr>
			<Id>SECACCCSDPXXYYAAA</Id>
			<Tp>
				<Cd>CSDP</Cd>
			</Tp>
			<OpngDt>2019-01-01</OpngDt>
			<HldInd>true</HldInd>
			<NegPos>false</NegPos>
			<EndInvstrFlg>NONE</EndInvstrFlg>
			<PricgSchme>SACC</PricgSchme>
		</SctiesAcct>
	</SctiesAcctCreReq>
</Document></Document>
```


## Nested source envelope

P342 and P343 each open Document, and P372 closes both. This is well-formed nested XML, but a namespace-only derived copy does not match the supplied schema. No wrapper was removed to make the source pass. The paired envelopes are also visible on Word pages32–33.

## Validation

| Paragraphs | XML syntax | Namespace-only derived schema validation |
| --- | --- | --- |
| P342–P372 | pass | fail |


[reda.018.001.01](../../../../messages/reda.018.001.01/index.md) · [Exact derivation and error evidence](../../../../../../../tracking/reviews/t2s-securities-account-reference-data.json)
