---
template: false
document_kind: "message-example"
review_status: "reviewed"
manual_curated: true
title: "CustomerCreditTransferInitiation pain.001.001.13"
domain: "payments"
source_ids: ["src-000173", "src-000176"]
message_sets: ["payments-initiation"]
message_ids: ["pain.001.001.13"]
message_families: ["pain.001"]
source_locations: [{"source_id": "src-000173", "locator": "P333–P541; T24", "heading_path": ["Business Examples", "CustomerCreditTransferInitiation pain.001.001.13"]}, {"source_id": "src-000176", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pain.001.001.13; /xs:schema/xs:element[@name=\"Document\"]"}]
issue_ids: []
limitations: ["This is a supplied source example, not an invented example or current commercial event.", "Printed snippet has payload root and no namespace/Document envelope. Schema check used a separately derived envelope and qualified all source element names; original payload text is unchanged."]
participant_ids: ["participant-src-000173-example-aaaa-bank-london", "participant-src-000173-example-abc-corporation-california", "participant-src-000173-example-abc-corporation-new-york", "participant-src-000173-example-bbbb-bank-new-york", "participant-src-000173-example-bbbb-bank-san-francisco", "participant-src-000173-example-dddd-bank-belgium", "participant-src-000173-example-def-electronics", "participant-src-000173-example-ghi-semiconductors"]
source_editions: ["2025-2026", "March 2026"]
---

# CustomerCreditTransferInitiation pain.001.001.13

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Source scenario

**P320** CustomerCreditTransferInitiation pain.001.001.13

**P321** Description

**P322** ABC Corporation, New York has received three invoices:

**P323** Invoice 1

**P324** An invoice with number 4562, dated 08 September 2012 from DEF Electronics, London: 10 million JPY needs to be paid to DEF Electronics account 23683707994215 with AAAA Bank, London (AAAAGB2L). ABC Corporation assigns reference ABC/4562/2012-09-08 to the payment. Payment transaction charges are shared between ABC Corporation and DEF Electronics.

**P325** Invoice 2

**P326** An invoice with number ABC-13679, dated 15 September 2012 from GHI Semiconductors, Brussels: 500,000 EUR needs to be paid to GHI Semiconductors account BE30001216371411 with DDDD Bank, Belgium (DDDDBEBB). ABC Corporation assigns reference ABC/ABC-13679/2012-09-15 to the payment. The accounts receivable department of GHI Semiconductors needs to be advised when the funds have been credited on the account on telephone number +32/2/2222222. GHI Semiconductors will bear all payment transaction charges.

**P327** Invoice 3

**P328** An invoice with number 987-AC, dated 27 September 2012, from their branch ABC Corporation, California: 1 million USD needs to be paid to the branch account 4895623 with BBBB Bank, San Francisco (BBBBUS66). ABC assigns a reference ABC/987-AC/2012-09-27 to the payment. Payment transaction charges are shared.

**P329** ABC Corporation holds an account 00125574999 with BBBB Bank, New York (BBBBUS33) and instructs its bank to execute payment of the invoices with a CustomerCreditTransferInitiation message.

**P330** Business Data

**P331** CustomerCreditTransferInitiation from ABC Corporation, New York to BBBB Bank, New York:

**P332** Message Instance

[Complete supplied Business Data table](../documents/src-000173/tables/tbl-0024.md) · [Literal extracted XML payload](../../../../../assets/src-000173/examples/example-01.xml)

## Validation and scope

On 2026-11-09, the literal snippet parsed as well-formed XML. A working copy with the stated message namespace and Document envelope passed validation against [src-000176](../../../../../../../raw-input/payments_initiation/pain.001.001.13.xsd). This proves the wrapped copy satisfies the supplied XSD; it does not add business-rule validation or assert table/XML value equality.

## Complete source payload

```xml
<CstmrCdtTrfInitn>
	<GrpHdr>
		<MsgId>ABC/120928/CCT001</MsgId>
		<CreDtTm>2012-09-28T14:07:00</CreDtTm>
		<NbOfTxs>3</NbOfTxs>
		<CtrlSum>11500000</CtrlSum>
		<InitgPty>
			<Nm>ABC Corporation</Nm>
			<PstlAdr>
				<StrtNm>Times Square</StrtNm>
				<BldgNb>7</BldgNb>
				<PstCd>NY 10036</PstCd>
				<TwnNm>New York</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</InitgPty>
	</GrpHdr>
	<PmtInf>
		<PmtInfId>ABC/086</PmtInfId>
		<PmtMtd>TRF</PmtMtd>
		<BtchBookg>false</BtchBookg>
		<ReqdExctnDt>
			<Dt>2012-09-29</Dt>
		</ReqdExctnDt>
		<Dbtr>
			<Nm>ABC Corporation</Nm>
			<PstlAdr>
				<StrtNm>Times Square</StrtNm>
				<BldgNb>7</BldgNb>
				<PstCd>NY 10036</PstCd>
				<TwnNm>New York</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</Dbtr>
		<DbtrAcct>
			<Id>
				<Othr>
					<Id>00125574999</Id>
				</Othr>
			</Id>
		</DbtrAcct>
		<DbtrAgt>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</DbtrAgt>
		<CdtTrfTxInf>
			<PmtId>
				<InstrId>ABC/120928/CCT001/01</InstrId>
				<EndToEndId>ABC/4562/2012-09-08</EndToEndId>
			</PmtId>
			<Amt>
				<InstdAmt Ccy="JPY">10000000</InstdAmt>
			</Amt>
			<ChrgBr>SHAR</ChrgBr>
			<CdtrAgt>
				<FinInstnId>
					<BICFI>AAAAGB2L</BICFI>
				</FinInstnId>
			</CdtrAgt>
			<Cdtr>
				<Nm>DEF Electronics</Nm>
				<PstlAdr>
					<AdrLine>Corn Exchange 5th Floor</AdrLine>
					<AdrLine>Mark Lane 55</AdrLine>
					<AdrLine>EC3R7NE London</AdrLine>
					<AdrLine>GB</AdrLine>
				</PstlAdr>
			</Cdtr>
			<CdtrAcct>
				<Id>
					<Othr>
						<Id>23683707994125</Id>
					</Othr>
				</Id>
			</CdtrAcct>
			<Purp>
				<Cd>GDDS</Cd>
			</Purp>
			<RmtInf>
				<Strd>
					<RfrdDocInf>
						<Tp>
							<CdOrPrtry>
								<Cd>CINV</Cd>
							</CdOrPrtry>
						</Tp>
						<Nb>4562</Nb>
						<RltdDt>
						<Tp>
							<Cd>INDA</Cd>
						</Tp>
						<Dt>2012-09-08</Dt>									
						</RltdDt>							
					</RfrdDocInf>
				</Strd>
			</RmtInf>
		</CdtTrfTxInf>
		<CdtTrfTxInf>
			<PmtId>
				<InstrId>ABC/120928/CCT001/2</InstrId>
				<EndToEndId>ABC/ABC-13679/2012-09-15</EndToEndId>
			</PmtId>
			<Amt>
				<InstdAmt Ccy="EUR">500000</InstdAmt>
			</Amt>
			<ChrgBr>CRED</ChrgBr>
			<CdtrAgt>
				<FinInstnId>
					<BICFI>DDDDBEBB</BICFI>
				</FinInstnId>
			</CdtrAgt>
			<Cdtr>
				<Nm>GHI Semiconductors</Nm>
				<PstlAdr>
					<StrtNm>Avenue Brugmann</StrtNm>
					<BldgNb>415</BldgNb>
					<PstCd>1180</PstCd>
					<TwnNm>Brussels</TwnNm>
					<Ctry>BE</Ctry>
				</PstlAdr>
			</Cdtr>
			<CdtrAcct>
				<Id>
					<IBAN>BE30001216371411</IBAN>
				</Id>
			</CdtrAcct>
			<InstrForCdtrAgt>
				<Cd>PHOB</Cd>
				<InstrInf>+32/2/2222222</InstrInf>
			</InstrForCdtrAgt>
			<Purp>
				<Cd>GDDS</Cd>
			</Purp>
			<RmtInf>
				<Strd>
					<RfrdDocInf>
						<Tp>
							<CdOrPrtry>
								<Cd>CINV</Cd>
							</CdOrPrtry>
						</Tp>
						<Nb>ABC-13679</Nb>
						<RltdDt>
						<Tp>
							<Cd>INDA</Cd>
						</Tp>
						<Dt>2012-09-15</Dt>									
						</RltdDt>						
					</RfrdDocInf>
				</Strd>
			</RmtInf>
		</CdtTrfTxInf>
		<CdtTrfTxInf>
			<PmtId>
				<InstrId>ABC/120928/CCT001/3</InstrId>
				<EndToEndId>ABC/987-AC/2012-09-27</EndToEndId>
			</PmtId>
			<Amt>
				<InstdAmt Ccy="USD">1000000</InstdAmt>
			</Amt>
			<ChrgBr>SHAR</ChrgBr>
			<CdtrAgt>
				<FinInstnId>
					<BICFI>BBBBUS66</BICFI>
				</FinInstnId>
			</CdtrAgt>
			<Cdtr>
				<Nm>ABC Corporation</Nm>
				<PstlAdr>
					<Dept>Treasury department</Dept>
					<StrtNm>Bush Street</StrtNm>
					<BldgNb>13</BldgNb>
					<PstCd>CA 94108</PstCd>
					<TwnNm>San Francisco</TwnNm>
					<Ctry>US</Ctry>
				</PstlAdr>
			</Cdtr>
			<CdtrAcct>
				<Id>
					<Othr>
						<Id>4895623</Id>
					</Othr>
				</Id>
			</CdtrAcct>
			<Purp>
				<Cd>INTC</Cd>
			</Purp>
			<RmtInf>
				<Strd>
					<RfrdDocInf>
						<Tp>
							<CdOrPrtry>
								<Cd>CINV</Cd>
							</CdOrPrtry>
						</Tp>
						<Nb>987-AC</Nb>
						<RltdDt>
						<Tp>
							<Cd>INDA</Cd>
						</Tp>
						<Dt>2012-09-27</Dt>									
						</RltdDt>						
					</RfrdDocInf>
				</Strd>
			</RmtInf>
		</CdtTrfTxInf>
	</PmtInf>
</CstmrCdtTrfInitn>
```

<!-- EXAMPLE-PARTICIPANT-abc-corporation-new-york -->
[ABC Corporation, New York](../../../../../../../shared/reference/participants/participant-src-000173-example-abc-corporation-new-york.md) — Holds account 00125574999 and instructs BBBB Bank New York to pay three invoices; receives technical/customer-profile acceptance status. (P322–331; P544–546; T24; T25)
<!-- /EXAMPLE-PARTICIPANT-abc-corporation-new-york -->

<!-- EXAMPLE-PARTICIPANT-def-electronics -->
[DEF Electronics, London](../../../../../../../shared/reference/participants/participant-src-000173-example-def-electronics.md) — Creditor for JPY10000000 invoice4562; charges shared; account serviced by AAAA Bank London. (P324; T24)
<!-- /EXAMPLE-PARTICIPANT-def-electronics -->

<!-- EXAMPLE-PARTICIPANT-ghi-semiconductors -->
[GHI Semiconductors, Brussels](../../../../../../../shared/reference/participants/participant-src-000173-example-ghi-semiconductors.md) — Creditor for EUR500000 invoice ABC-13679, bears transaction charges; accounts-receivable department is to be advised after credit. (P326; T24)
<!-- /EXAMPLE-PARTICIPANT-ghi-semiconductors -->

<!-- EXAMPLE-PARTICIPANT-abc-corporation-california -->
[ABC Corporation, California](../../../../../../../shared/reference/participants/participant-src-000173-example-abc-corporation-california.md) — Separate source branch creditor for USD1000000 invoice987-AC; account at BBBB Bank San Francisco; charges shared. Table postal address includes Treasury department. (P328; T24)
<!-- /EXAMPLE-PARTICIPANT-abc-corporation-california -->

<!-- EXAMPLE-PARTICIPANT-bbbb-bank-new-york -->
[BBBB Bank, New York](../../../../../../../shared/reference/participants/participant-src-000173-example-bbbb-bank-new-york.md) — Receives ABC Corporation initiation and sends CustomerPaymentStatusReport after technical validation/customer-profile acceptance. (P329–331; P544–546; T24–T25)
<!-- /EXAMPLE-PARTICIPANT-bbbb-bank-new-york -->

<!-- EXAMPLE-PARTICIPANT-aaaa-bank-london -->
[AAAA Bank, London](../../../../../../../shared/reference/participants/participant-src-000173-example-aaaa-bank-london.md) — Services DEF Electronics creditor account in the supplied first credit-transfer instruction. (P324; T24)
<!-- /EXAMPLE-PARTICIPANT-aaaa-bank-london -->

<!-- EXAMPLE-PARTICIPANT-dddd-bank-belgium -->
[DDDD Bank, Belgium](../../../../../../../shared/reference/participants/participant-src-000173-example-dddd-bank-belgium.md) — Services GHI Semiconductors creditor account in the second instruction. (P326; T24)
<!-- /EXAMPLE-PARTICIPANT-dddd-bank-belgium -->

<!-- EXAMPLE-PARTICIPANT-bbbb-bank-san-francisco -->
[BBBB Bank, San Francisco](../../../../../../../shared/reference/participants/participant-src-000173-example-bbbb-bank-san-francisco.md) — Services the ABC California branch creditor account in the third instruction. Same generic bank label does not collapse this named office with BBBB New York. (P328; T24)
<!-- /EXAMPLE-PARTICIPANT-bbbb-bank-san-francisco -->
