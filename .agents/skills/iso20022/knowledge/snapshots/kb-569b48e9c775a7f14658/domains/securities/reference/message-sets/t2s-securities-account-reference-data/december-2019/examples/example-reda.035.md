---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.035.001.01"]
source_locations: [{"source_id": "src-000371", "heading_path": ["Business Examples", "Securities Account Activity Advice - reda.035.001.01"], "first_paragraph": "P577", "last_paragraph": "P610", "rendered_file_pages": [39, 40]}]
issue_ids: []
limitations: ["The original has no namespace. Schema-validation results refer only to the explicitly derived namespace-assigned copy; the literal source XML is unchanged."]
---

# Securities Account Activity Advice - reda.035.001.01

[src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P577–P610; Word file pages 39–40. This is the literal source example. Original XML is retained without a namespace; schema testing below uses only an explicitly derived namespace assignment.

**P578** Description

**P579** The Securities Account Activity Advice message provides information on changes occurred for securities account reference data during the business day. In this example, it shows one change occurred on 2019-02-01 to the securities account SECACCCSDPXXYYAAA regarding the hold indicator value.

**P580** System date: 2019-02-01

**P581** Securities Account Identification ID: SECACCCSDPXXYYAAA

**P582** Field changed: HoldReleaseDefault

**P583** Old Filed Value: False

**P584** New Field Value: True

**P585** Timestamp of the Update performed: 2019-02-01T16:10:10

**P586** Message Instance

**P587–P609**

```xml
<Document>
	<SctiesAcctActvtyAdvc>
		<MsgHdr>
			<MsgId>SAMPLESACSTA</MsgId>
		</MsgHdr>
		<Pgntn>
			<PgNb>1</PgNb>
			<LastPgInd>true</LastPgInd>
		</Pgntn>
		<SctiesAcctActvty>
			<SysDt>2019-02-01</SysDt>
			<Chng>
				<SctiesAcctId>
					<Id>SECACCCSDPXXYYAAA</Id>
				</SctiesAcctId>
				<FldNm>HoldReleaseDefault</FldNm>
				<OdFldVal>False</OdFldVal>
				<NewFldVal>True</NewFldVal>
				<OprTmStmp>2019-02-01T16:10:10</OprTmStmp>
			</Chng>
		</SctiesAcctActvty>
	</SctiesAcctActvtyAdvc>
</Document>
```


## Validation

| Paragraphs | XML syntax | Namespace-only derived schema validation |
| --- | --- | --- |
| P587–P609 | pass | pass |


[reda.035.001.01](../../../../messages/reda.035.001.01/index.md) · [Exact derivation and error evidence](../../../../../../../tracking/reviews/t2s-securities-account-reference-data.json)
