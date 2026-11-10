---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.023.001.01"]
source_locations: [{"source_id": "src-000371", "heading_path": ["Business Examples", "Securities Account Modification Request - reda.023.001.01"], "first_paragraph": "P373", "last_paragraph": "P397", "rendered_file_pages": [33, 34]}]
issue_ids: []
limitations: ["The original has no namespace. Schema-validation results refer only to the explicitly derived namespace-assigned copy; the literal source XML is unchanged."]
---

# Securities Account Modification Request - reda.023.001.01

[src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P373–P397; Word file pages 33–34. This is the literal source example. Original XML is retained without a namespace; schema testing below uses only an explicitly derived namespace assignment.

**P374** Description

**P375** In this example, the instructing party wants to update the negative position flag of the securities account SECACCCSDPXXYYAAA.

**P376** Securities Account Identification: SECACCCSDPXXYYAAA

**P377** Negative position flag: true

**P379** Message Instance

**P380–P397**

```xml
<Document>
	<SctiesAcctModReq>
		<MsgHdr>
			<MsgId>SAMPLESACUPDATE</MsgId>
		</MsgHdr>	
		<AcctId>
			<Id>SECACCCSDPXXYYAAA</Id>
		</AcctId>
		<Mod>
			<ScpIndctn>UPDT</ScpIndctn>
			<ReqdMod>
				<SysSctiesAcct>
					<NegPos>true</NegPos>
				</SysSctiesAcct>
			</ReqdMod>
		</Mod>
	</SctiesAcctModReq>
</Document>
```


## Validation

| Paragraphs | XML syntax | Namespace-only derived schema validation |
| --- | --- | --- |
| P380–P397 | pass | pass |


[reda.023.001.01](../../../../messages/reda.023.001.01/index.md) · [Exact derivation and error evidence](../../../../../../../tracking/reviews/t2s-securities-account-reference-data.json)
