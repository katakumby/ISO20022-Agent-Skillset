---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.021.001.01"]
source_locations: [{"source_id": "src-000371", "heading_path": ["Business Examples", "Securities Account Report - reda.021.001.01"], "first_paragraph": "P524", "last_paragraph": "P576", "rendered_file_pages": [37, 38, 39]}]
issue_ids: []
limitations: ["The original has no namespace. Schema-validation results refer only to the explicitly derived namespace-assigned copy; the literal source XML is unchanged."]
---

# Securities Account Report - reda.021.001.01

[src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P524–P576; Word file pages 37–39. This is the literal source example. Original XML is retained without a namespace; schema testing below uses only an explicitly derived namespace assignment.

**P525** Description

**P526** The Securities Account Report message can be used as answer for:

**P527** Securities Account Reference Data Query;

**P528** Securities Account List Query.

**P529** performed using the Securities Account Query. This example shows the answer to the Securities Account List Query described in the chapter 7.5. The query returns only one securities account:

**P530** Securities Account Identification: SECACCCSDPXXYYAAA

**P531** Account owner Parent BIC: CSDAXXYYAAA

**P532** Account owner Party BIC: CSDPXXYYAAA 

**P533** End investor flag: NONE

**P534** Pricing scheme: SACC

**P536** Message Instance

**P537–P575**

```xml
<Document>
	<SctiesAcctRpt>
		<MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizQry>
				<MsgId>SAMPLESALIQUERY</MsgId>
			</OrgnlBizQry>
		</MsgHdr>
		<Pgntn>
			<PgNb>1</PgNb>
			<LastPgInd>true</LastPgInd>
		</Pgntn>
		<RptOrErr>
			<SctiesAcctRpt>
				<SctiesAcctId>
					<Id>SECACCCSDPXXYYAAA</Id>
				</SctiesAcctId>
				<SctiesAcctOrErr>
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
						<EndInvstrFlg>NONE</EndInvstrFlg>
						<PricgSchme>SACC</PricgSchme>
					</SctiesAcct>
				</SctiesAcctOrErr>
			</SctiesAcctRpt>
		</RptOrErr>
	</SctiesAcctRpt>
</Document>
```


## Validation

| Paragraphs | XML syntax | Namespace-only derived schema validation |
| --- | --- | --- |
| P537–P575 | pass | pass |


[reda.021.001.01](../../../../messages/reda.021.001.01/index.md) · [Exact derivation and error evidence](../../../../../../../evidence/archived/1371923b3cb2b1a498b71abb.md)
