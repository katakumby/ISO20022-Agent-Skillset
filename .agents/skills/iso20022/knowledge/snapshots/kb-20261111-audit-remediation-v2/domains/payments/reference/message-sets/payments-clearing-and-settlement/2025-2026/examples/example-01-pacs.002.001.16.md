---
template: false
document_kind: "message-example"
title: "FIToFIPaymentStatusReport  pacs.002.001.16"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000165"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.002.001.16"]
message_families: ["pacs.002"]
source_locations: [{"source_id": "src-000162", "locator": "P659–P731; T28", "heading_path": ["Business Examples", "FIToFIPaymentStatusReport  pacs.002.001.16"]}, {"source_id": "src-000165", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.002.001.16; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaaus29", "participant-src-000162-example-ababus23", "participant-src-000162-example-jones-4dbd8f5", "participant-src-000162-example-virgay-6e3f97e"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# FIToFIPaymentStatusReport  pacs.002.001.16

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P650** FIToFIPaymentStatusReport  pacs.002.001.16

**P651** Description

**P652** On 28 June 2015, ABABUS23 received a FIToFICustomerDirectDebit message from AAAAUS29. On 29 June 2015, ABABUS23 rejects the FIToFICustomerDirectDebit message by sending a FIToFIPaymentStatusReport message to AAAAUS29, referring to the original instruction and indicating the reason for the rejection.

**P653** Related Message Examples

**P654** The FIToFICustomerDirectDebit instruction from AAAAUS29 to ABABUS23 is included in the business example section of the FIToFICustomerDirectDebit message.

**P655** As AAAUS29 has not yet credited the account of its customer, Virgay, in turn, AAAAUS29 will send a CustomerPaymentStatusReport to inform Virgay of the rejection. This example is included in the business example section of the PaymentStatusReport message in the Payments Initiation Message Reference Guide.

**P656** Business Data

**P657** PaymentStatusReport from ABABUS23 to AAAAUS29:

**P658** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0028.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-01.xml) · [Source example flow](../flows/example-src-000162-01.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [ABABUS23](../../../../../../../shared/reference/participants/participant-src-000162-example-ababus23.md) | InstgAgt | /FIToFIPmtStsRpt/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaaus29.md) | InstdAgt | /FIToFIPmtStsRpt/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Jones](../../../../../../../shared/reference/participants/participant-src-000162-example-jones-4dbd8f5.md) | Dbtr | /FIToFIPmtStsRpt/TxInfAndSts/OrgnlTxRef/Dbtr/Pty/Nm |
| [Virgay](../../../../../../../shared/reference/participants/participant-src-000162-example-virgay-6e3f97e.md) | Cdtr | /FIToFIPmtStsRpt/TxInfAndSts/OrgnlTxRef/Cdtr/Pty/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.002.001.16 and wrapped in Document passed the exact supplied XSD src-000165. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table XML tag <RtrdIntrBkSttlmAmt>; instance uses <IntrBkSttlmAmt> in OrgnlTxRef.
- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FIToFIPmtStsRpt>
	<GrpHdr>
		<MsgId>ABABUS23-STATUS-456/04</MsgId>
		<CreDtTm>2015-06-29T09:56:00</CreDtTm>
		<InstgAgt>
			<FinInstnId>
				<BICFI>ABABUS23</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>AAAAUS29</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<OrgnlGrpInfAndSts>
		<OrgnlMsgId>AAAA100628-123v</OrgnlMsgId>
		<OrgnlMsgNmId>pacs.003.001.12</OrgnlMsgNmId>
		<OrgnlCreDtTm>2015-06-28T10:05:00</OrgnlCreDtTm>
	</OrgnlGrpInfAndSts>
	<TxInfAndSts>
		<StsId>AB/8568</StsId>
		<OrgnlEndToEndId>VA060327/0123</OrgnlEndToEndId>
		<OrgnlTxId>AAAAUS29/100628/ad458</OrgnlTxId>
		<TxSts>RJCT</TxSts>
		<StsRsnInf>
			<Orgtr>
				<Id>
					<OrgId>
						<AnyBIC>ABABUS23</AnyBIC>
					</OrgId>
				</Id>
			</Orgtr>
			<Rsn>
				<Cd>AM05</Cd>
			</Rsn>
		</StsRsnInf>
		<OrgnlTxRef>
			<IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>
			<IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>
			<ReqdColltnDt>2015-07-13</ReqdColltnDt>
			<MndtRltdInf>
				<DrctDbtMndt>
					<MndtId>VIRGAY123</MndtId>
				</DrctDbtMndt>
			</MndtRltdInf>
			<Dbtr>
				<Pty>
					<Nm>Jones</Nm>
					<PstlAdr>
						<StrtNm>Hudson Street</StrtNm>
						<BldgNb>19</BldgNb>
						<PstCd>NJ 07302</PstCd>
						<TwnNm>Jersey City</TwnNm>
						<Ctry>US</Ctry>
					</PstlAdr>
				</Pty>	
			</Dbtr>
			<Cdtr>
				<Pty>
					<Nm>Virgay</Nm>
					<PstlAdr>
						<StrtNm>Virginia Lane</StrtNm>
						<BldgNb>36</BldgNb>
						<PstCd>NJ 07311</PstCd>
						<TwnNm>Jersey City</TwnNm>
						<Ctry>US</Ctry>
					</PstlAdr>
				</Pty>
			</Cdtr>
		</OrgnlTxRef>
	</TxInfAndSts>
</FIToFIPmtStsRpt>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-01.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
