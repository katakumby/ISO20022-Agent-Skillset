---
template: false
document_kind: "message-example"
review_status: "reviewed"
manual_curated: true
title: "CustomerPaymentReversal pain.007.001.13"
domain: "payments"
source_ids: ["src-000173", "src-000178"]
message_sets: ["payments-initiation"]
message_ids: ["pain.007.001.13"]
message_families: ["pain.007"]
source_locations: [{"source_id": "src-000173", "locator": "P670–P762; T27", "heading_path": ["Business Examples", "CustomerPaymentReversal pain.007.001.13"]}, {"source_id": "src-000178", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pain.007.001.13; /xs:schema/xs:element[@name=\"Document\"]"}]
issue_ids: []
limitations: ["This is a supplied source example, not an invented example or current commercial event.", "Printed snippet has payload root and no namespace/Document envelope. Schema check used a separately derived envelope and qualified all source element names; original payload text is unchanged."]
participant_ids: ["participant-src-000173-example-aaaadeff", "participant-src-000173-example-bbbbde33", "participant-src-000173-example-ritcom", "participant-src-000173-example-schneider"]
source_editions: ["2025-2026", "March 2026"]
---

# CustomerPaymentReversal pain.007.001.13

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Source scenario

**P664** CustomerPaymentReversal pain.007.001.13

**P665** Description

**P666** On 17 June 2012, date of the collection from debtor Schneider, Ritcom electricity company realises that the direct debit instruction sent on 9 June 2012 was a duplicated instruction. As settlement of the direct debit already took place, Ritcom electricity company initiates a CustomerPaymentReversal message and sends it to its account servicer AAAADEFF. Any potential charges relating to this reversal payment, paid by Schneider, will be deducted from the next invoice.

**P667** Business Data

**P668** CustomerPaymentReversal from Ritcom to AAAADEFF :

**P669** Message Instance

[Complete supplied Business Data table](../documents/src-000173/tables/tbl-0027.md) · [Literal extracted XML payload](../../../../../assets/src-000173/examples/example-04.xml)

## Validation and scope

On 2026-11-09, the literal snippet parsed as well-formed XML. A working copy with the stated message namespace and Document envelope passed validation against [src-000178](../../../../../../../raw-input/payments_initiation/pain.007.001.13.xsd). This proves the wrapped copy satisfies the supplied XSD; it does not add business-rule validation or assert table/XML value equality.

## Complete source payload

```xml
<CstmrPmtRvsl>
	<GrpHdr>
		<MsgId>RIT-REV-20120617-456f</MsgId>
		<CreDtTm>2012-06-17T15:38:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<InitgPty>
			<Nm>Ritcom</Nm>
			<PstlAdr>
				<StrtNm>Schueman Strasse</StrtNm>
				<BldgNb>18</BldgNb>
				<PstCd>60017</PstCd>
				<TwnNm>Frankfurt am Main</TwnNm>
				<Ctry>DE</Ctry>
			</PstlAdr>
		</InitgPty>
		<DbtrAgt>
			<FinInstnId>
				<BICFI>BBBBDE33</BICFI>
			</FinInstnId>
		</DbtrAgt>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>AAAADEFF</BICFI>
			</FinInstnId>
		</CdtrAgt>
	</GrpHdr>
	<OrgnlGrpInf>
		<OrgnlMsgId>RITCOM1234</OrgnlMsgId>
		<OrgnlMsgNmId>pain.008.001.12</OrgnlMsgNmId>
		<OrgnlCreDtTm>2012-06-09T09:18:00</OrgnlCreDtTm>
	</OrgnlGrpInf>
	<OrgnlPmtInfAndRvsl>
		<OrgnlPmtInfId>RIT/0053</OrgnlPmtInfId>
		<TxInf>
			<RvslId>RIT5467</RvslId>
			<OrgnlEndToEndId>RIT/012010-2562C26</OrgnlEndToEndId>
			<OrgnlInstdAmt Ccy="EUR">286</OrgnlInstdAmt>
			<RvsdInstdAmt Ccy="EUR">286</RvsdInstdAmt>
			<RvslRsnInf>
				<Orgtr>
					<Nm>Ritcom</Nm>
					<PstlAdr>
						<StrtNm>Schueman Strasse</StrtNm>
						<BldgNb>18</BldgNb>
						<PstCd>60017</PstCd>
						<TwnNm>Frankfurt am Main</TwnNm>
						<Ctry>DE</Ctry>
					</PstlAdr>
				</Orgtr>
				<Rsn>
					<Cd>AM05</Cd>
				</Rsn>
			</RvslRsnInf>
			<OrgnlTxRef>
				<ReqdColltnDt>2010-06-16</ReqdColltnDt>
				<MndtRltdInf>
					<DrctDbtMndt>
						<MndtId>RIT04/av002</MndtId>
					</DrctDbtMndt>
				</MndtRltdInf>
				<Dbtr>
					<Pty>
						<Nm>Schneider</Nm>
						<PstlAdr>
							<StrtNm>Kuertman Strasse</StrtNm>
							<BldgNb>45</BldgNb>
							<PstCd>50475</PstCd>
							<TwnNm>Koln</TwnNm>
							<Ctry>DE</Ctry>
						</PstlAdr>
					</Pty>
				</Dbtr>
				<DbtrAcct>
					<Id>
						<IBAN>DE89370400440332014000</IBAN>
					</Id>
				</DbtrAcct>
				<Cdtr>
					<Pty>
						<Nm>Ritcom</Nm>
						<PstlAdr>
							<StrtNm>Schueman Strasse</StrtNm>
							<BldgNb>18</BldgNb>
							<PstCd>60017</PstCd>
							<TwnNm>Frankfurt am Main</TwnNm>
							<Ctry>DE</Ctry>
						</PstlAdr>
					</Pty>
				</Cdtr>
			</OrgnlTxRef>
		</TxInf>
	</OrgnlPmtInfAndRvsl>
</CstmrPmtRvsl>
```

<!-- EXAMPLE-PARTICIPANT-ritcom -->
[Ritcom](../../../../../../../shared/reference/participants/participant-src-000173-example-ritcom.md) — Electricity company reverses an already settled duplicate direct debit; any reversal charges paid by Schneider are deducted from next invoice. (P666–668; T27)
<!-- /EXAMPLE-PARTICIPANT-ritcom -->

<!-- EXAMPLE-PARTICIPANT-schneider -->
[Schneider](../../../../../../../shared/reference/participants/participant-src-000173-example-schneider.md) — Debtor in Ritcom duplicate-direct-debit reversal example; original/reversed amount EUR286 and account data appear in T27. (P666; T27)
<!-- /EXAMPLE-PARTICIPANT-schneider -->

<!-- EXAMPLE-PARTICIPANT-aaaadeff -->
[AAAADEFF](../../../../../../../shared/reference/participants/participant-src-000173-example-aaaadeff.md) — Ritcom account servicer receives CustomerPaymentReversal in the supplied example. (P666–668; T27)
<!-- /EXAMPLE-PARTICIPANT-aaaadeff -->

<!-- EXAMPLE-PARTICIPANT-bbbbde33 -->
[BBBBDE33](../../../../../../../shared/reference/participants/participant-src-000173-example-bbbbde33.md) — Debtor agent identified in the source reversal business-data table and XML. (T27; P686–690)
<!-- /EXAMPLE-PARTICIPANT-bbbbde33 -->
