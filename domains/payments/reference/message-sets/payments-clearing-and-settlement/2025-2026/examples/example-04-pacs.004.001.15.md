---
template: false
document_kind: "message-example"
title: "Second PaymentReturn"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000167"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.004.001.15"]
message_families: ["pacs.004"]
source_locations: [{"source_id": "src-000162", "locator": "P906–P966; T31", "heading_path": ["Business Examples", "PaymentReturn pacs.004.001.15 - 1", "Second PaymentReturn"]}, {"source_id": "src-000167", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-bbbbie2d", "participant-src-000162-example-ccccie2d", "participant-src-000162-example-seed-inc-0785746"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# Second PaymentReturn

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Source scenario

**P900** Second PaymentReturn

**P901** Description

**P902** On receipt of the payment return message from CCCC Bank, BBBB Bank deducts processing charges for the return message, credits the account of AAAA Bank and forwards the payment return message to AAAA Bank.

**P903** Business Data

**P904** PaymentReturn from BBBB Bank to AAAA Bank:

**P905** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0031.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-04.xml) · [Source example flow](../flows/example-src-000162-03.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | InstgAgt | /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | InstdAgt | /PmtRtr/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | Agt | /PmtRtr/TxInf/ChrgsInf[1]/Agt/FinInstnId/BICFI |
| [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | Agt | /PmtRtr/TxInf/ChrgsInf[2]/Agt/FinInstnId/BICFI |
| [Seed Inc.](../../../../../../../shared/reference/participants/participant-src-000162-example-seed-inc-0785746.md) | Orgtr | /PmtRtr/TxInf/RtrRsnInf/Orgtr/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15 and wrapped in Document passed the exact supplied XSD src-000167. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table tag <AddtlRtrRsnInf>; XML RtrRsnInf/AddtlInf.

## Complete source payload

```xml
<PmtRtr>
	<GrpHdr>
		<MsgId>BBBB/151122-PR05</MsgId>
		<CreDtTm>2015-11-22T11:15:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>INGA</SttlmMtd>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>BBBBIE2D</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>AAAAGB2L</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<OrgnlGrpInf>
		<OrgnlMsgId>AAAA/151109-CCT/EUR443</OrgnlMsgId>
		<OrgnlMsgNmId>pacs.008.001.12</OrgnlMsgNmId>
		<OrgnlCreDtTm>2015-11-09T10:03:13</OrgnlCreDtTm>
	</OrgnlGrpInf>
	<TxInf>
		<RtrId>BBBB/151122-PR05/1</RtrId>
		<OrgnlInstrId>AAAA/151109-CCT/EUR443/1</OrgnlInstrId>
		<OrgnlEndToEndId>CROPS/SX-25T/2015-10-13</OrgnlEndToEndId>
		<OrgnlTxId>AAAA/151109-CCT/EUR443/1</OrgnlTxId>
		<OrgnlIntrBkSttlmAmt Ccy="EUR">75000</OrgnlIntrBkSttlmAmt>
		<RtrdIntrBkSttlmAmt Ccy="EUR">74650</RtrdIntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-11-22</IntrBkSttlmDt>
		<RtrdInstdAmt Ccy="EUR">74850</RtrdInstdAmt>
		<ChrgBr>CRED</ChrgBr>
		<ChrgsInf>
			<Amt Ccy="EUR">100</Amt>
			<Agt>
				<FinInstnId>
					<BICFI>CCCCIE2D</BICFI>
				</FinInstnId>
			</Agt>
		</ChrgsInf>
		<ChrgsInf>
			<Amt Ccy="EUR">100</Amt>
			<Agt>
				<FinInstnId>
					<BICFI>BBBBIE2D</BICFI>
				</FinInstnId>
			</Agt>
		</ChrgsInf>
		<RtrRsnInf>
			<Orgtr>
				<Nm>Seed Inc.</Nm>
			</Orgtr>
			<Rsn>
				<Cd>NARR</Cd>
			</Rsn>
			<AddtlInf>RETURN AFTER ACCEPTED PAYMENT CANCELLATION REQUEST</AddtlInf>
		</RtrRsnInf>
	</TxInf>
</PmtRtr>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-03.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
