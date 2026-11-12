---
template: false
document_kind: "message-example"
review_status: "needs-review"
manual_curated: true
title: "CustomerPaymentStatusReport pain.002.001.15 - 2"
domain: "payments"
source_ids: ["src-000173", "src-000177"]
message_sets: ["payments-initiation"]
message_ids: ["pain.002.001.15"]
message_families: ["pain.002"]
source_locations: [{"source_id": "src-000173", "locator": "P583–P663; T26", "heading_path": ["Business Examples", "CustomerPaymentStatusReport pain.002.001.15 - 2"]}, {"source_id": "src-000177", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pain.002.001.15; /xs:schema/xs:element[@name=\"Document\"]"}]
issue_ids: ["issue-000052"]
limitations: ["This is a supplied source example, not an invented example or current commercial event.", "Printed snippet has payload root and no namespace/Document envelope. Schema check used a separately derived envelope and qualified all source element names; original payload text is unchanged."]
participant_ids: ["participant-src-000173-example-aaaaus29", "participant-src-000173-example-ababus23", "participant-src-000173-example-jones", "participant-src-000173-example-virgay"]
source_editions: ["2025-2026", "March 2026"]
---

# CustomerPaymentStatusReport pain.002.001.15 - 2

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Source scenario

**P577** CustomerPaymentStatusReport pain.002.001.15 - 2

**P578** Description

**P579** AAAAUS29 received an FIToFIPaymentStatusReport from its correspondent, ABABUS23, containing reject information about a previously sent FIToFICustomerDirectDebit. As AAAAUS29 has not yet credited the account of the original initiating party (Virgay) of the direct debit, AAAAUS29 in its turn informs Virgay about the rejection of the CustomerDirectDebitInitiation sent on 28 June 2012.

**P580** Business Description

**P581** CustomerPaymentStatusReport from AAAAUS29 to Virgay:

**P582** Message Instance

[Complete supplied Business Data table](../documents/src-000173/tables/tbl-0026.md) · [Literal extracted XML payload](../../../../../assets/src-000173/examples/example-03.xml)

## Validation and scope

On 2026-11-09, the literal snippet parsed as well-formed XML. A working copy with the stated message namespace and Document envelope passed validation against [src-000177](../../../../../../../raw-input/payments_initiation/pain.002.001.15.xsd). This proves the wrapped copy satisfies the supplied XSD; it does not add business-rule validation or assert table/XML value equality.

The StatusID table/XML difference remains issue-000052: T26 row23 cell3 RJT2012_657B versus P611 RIT2012 657B.

## Complete source payload

```xml
<CstmrPmtStsRpt>
	<GrpHdr>
		<MsgId>AAAAUS29_5678c</MsgId>
		<CreDtTm>2012-06-29T15:49:00</CreDtTm>
		<InitgPty>
			<Nm>Virgay</Nm>
			<PstlAdr>
				<StrtNm>Virginia Lane</StrtNm>
				<BldgNb>36</BldgNb>
				<PstCd>NJ 07311</PstCd>
				<TwnNm>Jersey City</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</InitgPty>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>AAAAUS29</BICFI>
			</FinInstnId>
		</CdtrAgt>
	</GrpHdr>
	<OrgnlGrpInfAndSts>
		<OrgnlMsgId>CAVAY1234</OrgnlMsgId>
		<OrgnlMsgNmId>pain.008.001.12</OrgnlMsgNmId>
		<OrgnlCreDtTm>2012-06-28T14:25:00</OrgnlCreDtTm>
	</OrgnlGrpInfAndSts>
	<OrgnlPmtInfAndSts>
		<OrgnlPmtInfId>JKL_774</OrgnlPmtInfId>
		<TxInfAndSts>
			<StsId>RIT2012 657B</StsId>
			<OrgnlEndToEndId>VA100327/0123</OrgnlEndToEndId>
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
				<Amt>
					<InstdAmt Ccy="USD">1025</InstdAmt>
				</Amt>
				<ReqdColltnDt>2012-07-02</ReqdColltnDt>
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
	</OrgnlPmtInfAndSts>
</CstmrPmtStsRpt>
```

<!-- EXAMPLE-PARTICIPANT-virgay -->
[Virgay](../../../../../../../shared/reference/participants/participant-src-000173-example-virgay.md) — Insurance company sends two direct-debit collections under VERPA-1; in a separate rejection example receives status before original creditor account was credited. Contactdetails names J. Thompson. (P579–581; P765–771; T26; T28)
<!-- /EXAMPLE-PARTICIPANT-virgay -->

<!-- EXAMPLE-PARTICIPANT-aaaaus29 -->
[AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000173-example-aaaaus29.md) — Services Virgay and receives direct-debit initiation; receives correspondent rejection and informs Virgay before crediting its account in the rejection example. (P579–581; P765; T26; T28)
<!-- /EXAMPLE-PARTICIPANT-aaaaus29 -->

<!-- EXAMPLE-PARTICIPANT-ababus23 -->
[ABABUS23](../../../../../../../shared/reference/participants/participant-src-000173-example-ababus23.md) — Correspondent of AAAAUS29 sends FIToFIPaymentStatusReport rejecting previously sent interbank direct debit. T26 status-reason originator contains this AnyBIC. (P579; T26)
<!-- /EXAMPLE-PARTICIPANT-ababus23 -->

<!-- EXAMPLE-PARTICIPANT-jones -->
[Jones](../../../../../../../shared/reference/participants/participant-src-000173-example-jones.md) — Debtor for recurring yearly USD1025 life-insurance collection; mandate VIRGAY123 signed13July2008, final collection13July2015. A separate rejection example includes Jones in original transaction reference. (P767; T26; T28)
<!-- /EXAMPLE-PARTICIPANT-jones -->
