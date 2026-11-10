---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.020.001.01"]
source_locations: [{"source_id": "src-000371", "heading_path": ["Business Examples", "Securities Account Status Advice - reda.020.001.01"], "first_paragraph": "P414", "last_paragraph": "P495", "rendered_file_pages": [34, 35, 36]}]
issue_ids: []
limitations: ["The original has no namespace. Schema-validation results refer only to the explicitly derived namespace-assigned copy; the literal source XML is unchanged."]
---

# Securities Account Status Advice - reda.020.001.01

[src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P414–P495; Word file pages 34–36. This is the literal source example. Original XML is retained without a namespace; schema testing below uses only an explicitly derived namespace assignment.

**P415** Description

**P416** The following examples are referred to the status advice related to the Securities Account Deletion Request of the chapter 7.3. in three different cases:

**P417** Deletion completed successfully;

**P418** Deletion queued;

**P419** Deletion rejected.

**P420** Completed example

**P421** Description

**P422** In this case the Securities Account Deletion Request has been successfully executed.

**P423** Original Message ID: SAMPLESACDELETE

**P424** Securities Account Identification: SECACCCSDPXXYYAAA

**P425** Status: COMP

**P426** Message Instance

**P427–P442**

```xml
<Document>
	<SctiesAcctStsAdvc>
		<MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizInstr>
				<MsgId>SAMPLESACDELETE</MsgId>
			</OrgnlBizInstr>
		</MsgHdr>	
		<SctiesAcctSts>
			<RltdSctiesAcct>
				<Id>SECACCCSDPXXYYAAA</Id>
			</RltdSctiesAcct>
			<Sts>COMP</Sts>
		</SctiesAcctSts>
	</SctiesAcctStsAdvc>
</Document>
```

**P443** Queued example

**P444** Description

**P445** This example describes the case in which the Securities Account Deletion Request has been delayed. In case of for example a night-time cycle is running.  

**P446** Original Message ID: SAMPLESACDELETE

**P447** Status: QUED

**P448** Additional Information: UPDATE QUEUED

**P450** Message Instance

**P451–P469**

```xml
<Document>
	<SctiesAcctStsAdvc>
		<MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizInstr>
				<MsgId>SAMPLESACDELETE</MsgId>
			</OrgnlBizInstr>
		</MsgHdr>
		<SctiesAcctSts>
			<Sts>QUED</Sts>
			<StsRsn>
				<Rsn>
					<Prtry>QUED</Prtry>
				</Rsn>
				<AddtlInf>UPDATE QUEUED</AddtlInf>
			</StsRsn>
		</SctiesAcctSts>
	</SctiesAcctStsAdvc>
</Document>
```

**P470** Rejected example

**P471** Description

**P472** In this example the Securities Account Status Advice reports that the Securities Account Deletion Request has been rejected, specifying the rejection reason.

**P473** Original Message ID: SAMPLESACDELETE

**P474** Status. REJT

**P475** Additional Information: ABCD000 DELETION REJECTED

**P476** Message Instance

**P477–P495**

```xml
<Document>
	<SctiesAcctStsAdvc>
		<MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizInstr>
				<MsgId>SAMPLESACDELETE</MsgId>
			</OrgnlBizInstr>
		</MsgHdr>
		<SctiesAcctSts>
			<Sts>REJT</Sts>
			<StsRsn>
				<Rsn>
					<Prtry>REJT</Prtry>
				</Rsn>
				<AddtlInf>ABCD000 DELETION REJECTED</AddtlInf>
			</StsRsn>
		</SctiesAcctSts>
	</SctiesAcctStsAdvc>
</Document>
```


## Validation

| Paragraphs | XML syntax | Namespace-only derived schema validation |
| --- | --- | --- |
| P427–P442 | pass | pass |
| P451–P469 | pass | pass |
| P477–P495 | pass | pass |


[reda.020.001.01](../../../../messages/reda.020.001.01/index.md) · [Exact derivation and error evidence](../../../../../../../tracking/reviews/t2s-securities-account-reference-data.json)
