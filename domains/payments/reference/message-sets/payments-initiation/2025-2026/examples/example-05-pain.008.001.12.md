---
template: false
document_kind: "message-example"
review_status: "reviewed"
manual_curated: true
title: "CustomerDirectDebitInitiation pain.008.001.12 "
domain: "payments"
source_ids: ["src-000173", "src-000179"]
message_sets: ["payments-initiation"]
message_ids: ["pain.008.001.12"]
message_families: ["pain.008"]
source_locations: [{"source_id": "src-000173", "locator": "P773–P918; T28", "heading_path": ["Business Examples", "CustomerDirectDebitInitiation pain.008.001.12 "]}, {"source_id": "src-000179", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pain.008.001.12; /xs:schema/xs:element[@name=\"Document\"]"}]
issue_ids: []
limitations: ["This is a supplied source example, not an invented example or current commercial event.", "Printed snippet has payload root and no namespace/Document envelope. Schema check used a separately derived envelope and qualified all source element names; original payload text is unchanged."]
participant_ids: ["participant-src-000173-example-aaaaus29", "participant-src-000173-example-bbbbus39", "participant-src-000173-example-ccccus27", "participant-src-000173-example-jones", "participant-src-000173-example-lee", "participant-src-000173-example-virgay"]
source_editions: ["2025-2026", "March 2026"]
---

# CustomerDirectDebitInitiation pain.008.001.12 

[src-000173](../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Source scenario

**P763** CustomerDirectDebitInitiation pain.008.001.12

**P764** Narrative

**P765** On 2 June 2012, Virgay insurance company sends a CustomerDirectDebitInitiation message to its account servicer, AAAAUS29. AAAAUS29 offers a special service to Virgay, under agreement VERPA-1.

**P766** The direct debit initiation message contains two collection instructions from two different debtors.

**P767** The first direct debit instruction is for 1025 USD to be collected from account 123456, owned by debtor Jones and serviced by agent BBBBUS39. The mandate reference is VIRGAY123 and was signed by Jones on 13 July 2008. The last collection is due to take place on 13 July 2015. The payment is for a yearly life insurance fee.

**P768** The second direct debit instruction is for 985 USD to be collected from account 789101, owned by debtor Lee and serviced by agent CCCCUS27. This is a one-off direct debit which was notified to Lee on 8 June 2012, with reference VIRGAY2435/2012. The payment is for a car insurance premium.

**P769** The requested collection date for both collections is 13 July 2012 and charges related to the handling of the instruction will be shared between Virgay insurance company and the debtors.

**P770** Business Data

**P771** CustomerDirectDebitInitiation from Virgay to AAAAUS29:

**P772** Message Instance

[Complete supplied Business Data table](../documents/src-000173/tables/tbl-0028.md) · [Literal extracted XML payload](../../../../../assets/src-000173/examples/example-05.xml)

## Validation and scope

On 2026-11-09, the literal snippet parsed as well-formed XML. A working copy with the stated message namespace and Document envelope passed validation against [src-000179](../../../../../../../raw-input/payments_initiation/pain.008.001.12.xsd). This proves the wrapped copy satisfies the supplied XSD; it does not add business-rule validation or assert table/XML value equality.

## Complete source payload

```xml
<CstmrDrctDbtInitn>
	<GrpHdr>
		<MsgId>CAVAY1234</MsgId>
		<CreDtTm>2012-06-02T14:25:00</CreDtTm>
		<NbOfTxs>2</NbOfTxs>
		<CtrlSum>2010</CtrlSum>
		<InitgPty>
			<Nm>Virgay</Nm>
			<PstlAdr>
				<StrtNm>Virginia Lane</StrtNm>
				<BldgNb>36</BldgNb>
				<PstCd>NJ 07311</PstCd>
				<TwnNm>Jersey City</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
			<CtctDtls>
				<Nm>J. Thompson</Nm>
				<EmailAdr>Thompson@virgay.com</EmailAdr>
			</CtctDtls>
		</InitgPty>
	</GrpHdr>
	<PmtInf>
		<PmtInfId>CAVAY/88683</PmtInfId>
		<PmtMtd>DD</PmtMtd>
		<BtchBookg>false</BtchBookg>
		<ReqdColltnDt>2012-07-13</ReqdColltnDt>
		<Cdtr>
			<Nm>Virgay</Nm>
			<PstlAdr>
				<StrtNm>Virginia Lane</StrtNm>
				<BldgNb>36</BldgNb>
				<PstCd>NJ 07311</PstCd>
				<TwnNm>Jersey City</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<Othr>
					<Id>789123</Id>
				</Othr>
			</Id>
		</CdtrAcct>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>AAAAUS29</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<DrctDbtTxInf>
			<PmtId>
				<EndToEndId>VA060327/0123</EndToEndId>
			</PmtId>
			<PmtTpInf>
				<InstrPrty>NORM</InstrPrty>
				<SvcLvl>
					<Prtry>VERPA-1</Prtry>
				</SvcLvl>
				<SeqTp>RCUR</SeqTp>
			</PmtTpInf>
			<InstdAmt Ccy="USD">1025</InstdAmt>
			<ChrgBr>SHAR</ChrgBr>
			<DrctDbtTx>
				<MndtRltdInf>
					<MndtId>VIRGAY123</MndtId>
					<DtOfSgntr>2008-07-13</DtOfSgntr>
					<FnlColltnDt>2015-07-13</FnlColltnDt>
					<Frqcy><Tp>YEAR</Tp></Frqcy>
				</MndtRltdInf>
			</DrctDbtTx>
			<DbtrAgt>
				<FinInstnId>
					<BICFI>BBBBUS39</BICFI>
				</FinInstnId>
			</DbtrAgt>
			<Dbtr>
				<Nm>Jones</Nm>
				<PstlAdr>
					<StrtNm>Hudson Street</StrtNm>
					<BldgNb>19</BldgNb>
					<PstCd>NJ 07302</PstCd>
					<TwnNm>Jersey City</TwnNm>
					<Ctry>US</Ctry>
				</PstlAdr>
			</Dbtr>
			<DbtrAcct>
				<Id>
					<Othr>
						<Id>123456</Id>
					</Othr>
				</Id>
			</DbtrAcct>
			<Purp>
				<Cd>LIFI</Cd>
			</Purp>
			<RmtInf>
				<Ustrd>LIFE INSURANCE PAYMENT/ JULY 2012</Ustrd>
			</RmtInf>
		</DrctDbtTxInf>
		<DrctDbtTxInf>
			<PmtId>
				<EndToEndId>AY090327/456</EndToEndId>
			</PmtId>
			<PmtTpInf>
				<InstrPrty>NORM</InstrPrty>
				<SvcLvl>
					<Prtry>VERPA-1</Prtry>
				</SvcLvl>
				<SeqTp>OOFF</SeqTp>
			</PmtTpInf>
			<InstdAmt Ccy="USD">985</InstdAmt>
			<ChrgBr>SHAR</ChrgBr>
			<DrctDbtTx>
				<PreNtfctnId>VIRGAY2435/2012</PreNtfctnId>
				<PreNtfctnDt>2012-06-08</PreNtfctnDt>
			</DrctDbtTx>
			<DbtrAgt>
				<FinInstnId>
					<BICFI>CCCCUS27</BICFI>
				</FinInstnId>
			</DbtrAgt>
			<Dbtr>
				<Nm>Lee</Nm>
				<PstlAdr>
					<StrtNm>Cross Road</StrtNm>
					<BldgNb>45</BldgNb>
					<PstCd>NJ07399</PstCd>
					<TwnNm>Jersey City</TwnNm>
					<Ctry>US</Ctry>
				</PstlAdr>
			</Dbtr>
			<DbtrAcct>
				<Id>
					<Othr>
						<Id>789101</Id>
					</Othr>
				</Id>
			</DbtrAcct>
			<RmtInf>
				<Ustrd>CAR INSURANCE PREMIUM</Ustrd>
			</RmtInf>
		</DrctDbtTxInf>
	</PmtInf>
</CstmrDrctDbtInitn>
```

<!-- EXAMPLE-PARTICIPANT-virgay -->
[Virgay](../../../../../../../shared/reference/participants/participant-src-000173-example-virgay.md) — Insurance company sends two direct-debit collections under VERPA-1; in a separate rejection example receives status before original creditor account was credited. Contactdetails names J. Thompson. (P579–581; P765–771; T26; T28)
<!-- /EXAMPLE-PARTICIPANT-virgay -->

<!-- EXAMPLE-PARTICIPANT-aaaaus29 -->
[AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000173-example-aaaaus29.md) — Services Virgay and receives direct-debit initiation; receives correspondent rejection and informs Virgay before crediting its account in the rejection example. (P579–581; P765; T26; T28)
<!-- /EXAMPLE-PARTICIPANT-aaaaus29 -->

<!-- EXAMPLE-PARTICIPANT-jones -->
[Jones](../../../../../../../shared/reference/participants/participant-src-000173-example-jones.md) — Debtor for recurring yearly USD1025 life-insurance collection; mandate VIRGAY123 signed13July2008, final collection13July2015. A separate rejection example includes Jones in original transaction reference. (P767; T26; T28)
<!-- /EXAMPLE-PARTICIPANT-jones -->

<!-- EXAMPLE-PARTICIPANT-bbbbus39 -->
[BBBBUS39](../../../../../../../shared/reference/participants/participant-src-000173-example-bbbbus39.md) — Services Jones account for the recurring direct-debit collection. (P767; T28)
<!-- /EXAMPLE-PARTICIPANT-bbbbus39 -->

<!-- EXAMPLE-PARTICIPANT-lee -->
[Lee](../../../../../../../shared/reference/participants/participant-src-000173-example-lee.md) — Debtor for one-off USD985 car-insurance collection, pre-notified8June2012 with reference VIRGAY2435/2012. (P768; T28)
<!-- /EXAMPLE-PARTICIPANT-lee -->

<!-- EXAMPLE-PARTICIPANT-ccccus27 -->
[CCCCUS27](../../../../../../../shared/reference/participants/participant-src-000173-example-ccccus27.md) — Services Lee account in the one-off direct-debit collection. (P768; T28)
<!-- /EXAMPLE-PARTICIPANT-ccccus27 -->
