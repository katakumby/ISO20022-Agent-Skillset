---
template: false
document_kind: "message-example"
title: "FIToFICustomerCreditTransfer pacs.008.001.14 - 1"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000169"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1284–P1392; T35", "heading_path": ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 1", "First FIToFICustomerCreditTransfer"]}, {"source_id": "src-000169", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-aaaajpjt", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-ccccjpjt", "participant-src-000162-example-def-electronics-bf4c618"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# FIToFICustomerCreditTransfer pacs.008.001.14 - 1

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P1259** FIToFICustomerCreditTransfer pacs.008.001.14 - 1

**P1260** This example covers four FIToFICustomerCreditTransfer messages sent by BBBBUS33.

**P1261** The first FIToFICustomerCreditTransfer message is sent to AAAAGB2L.

**P1262** The second FIToFICustomerCreditTransfer message is sent to EEEEDEFF.

**P1263** The third FIToFICustomerCreditTransfer is sent to BBBBUS66

**P1264** A fourth FIToFICustomerCreditTransfer message, sent by EEEEDEFF to DDDDBEBB, is also shown.

**P1265** Description

**P1266** BBBB Bank, New York, has received a payment initiation from its client ABC Corporation, New York, that holds an account 00125574999 with them for payment of the following invoices:

**P1267** Invoice 1

**P1268** An invoice with number 4562, dated 08 September 2015 from DEF Electronics, London: 10 million JPY needs to be paid to DEF Electronics account 23683707994215 with AAAA Bank, London (AAAAGB2L). ABC Corporation assigns reference ABC/4562/2015-09-08 to the payment. Payment transaction charges are shared between ABC Corporation and DEF Electronics.

**P1269** Invoice 2

**P1270** An invoice with number ABC-13679, dated 15 September 2015 from GHI Semiconductors, Brussels: 500,000 EUR needs to be paid to GHI Semiconductors account BE30001216371411 with DDDD Bank, Belgium (DDDDBEBB). ABC Corporation assigns reference ABC/ABC-13679/2015-09-15 to the payment. The accounts receivable department of GHI Semiconductors needs to be advised when the funds have been credited to the account on telephone number +32/2/2222222. GHI Semiconductors will bear all payment transaction charges.

**P1271** Invoice 3

**P1272** An invoice with number 987-AC, dated 27 September 2015 from their branch ABC Corporation, California: 1 million USD needs to be paid on the branch account 4895623 with BBBB Bank, San Francisco (BBBBUS66). ABC assigns reference ABC/987-AC/2015-09-27 to the payment. Payment transaction charges are shared.

**P1273** Related Message Examples

**P1274** ABC Corporation sent a CustomerCreditTransferInitiation message containing the 3 transactions to BBBB Bank. This is illustrated in the CustomerCreditTransferInitiation business example section of the Payments Initiation Message Reference Guide.

**P1275** To process the three payment instructions, BBBB Bank sends three FIToFICustomerCreditTransfer messages:

**P1276** A first message to AAAA Bank, London (AAAAGB2L). As the banks do not have a JPY account relationship, the payment is processed using the cover method. The JPY correspondent of BBBB Bank is CCCC Bank, Tokyo (CCCCJPJT). The JPY correspondent of AAAA Bank, London is AAAA Bank, Tokyo (AAAAJPJT). For the reimbursement instruction sent by BBBB Bank to its JPY correspondent CCCC Bank, please refer to the FinancialInstitutionCreditTransfer business example 1.

**P1277** A second message to its EUR correspondent EEEE Bank, Frankfurt (EEEEDEFF) where BBBB Bank has multiple accounts, for payment to DDDDBEBB. BBBB Bank specifies that account 29314569847 should be used for reimbursement.

**P1278** BBBB Bank has also received a payment order from their client Mr. Jones requesting to pay a 5 thousand EUR insurance premium by 30 September 2006 for contract ZZ/JO/164794 to ZZ Insurances, Frankfurt on their account DE89370400440532014000 with EEEEDEFF. Charges will be shared between the parties. BBBB Bank decides to include the latter 2 transactions in one FIToFICustomerCreditTransfer message.

**P1279** A third message is send to its branch BBBB Bank, San Francisco and instructs its branch to credit the account of ABC Corporation California in their books, account number 4895623.

**P1280** First FIToFICustomerCreditTransfer

**P1281** Business Data

**P1282** The first FIToFICustomerCreditTransfer message, from BBBBUS33 to AAAAGB2L:

**P1283** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0035.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-08.xml) · [Source example flow](../flows/example-src-000162-08.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [CCCCJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccjpjt.md) | InstgRmbrsmntAgt | /FIToFICstmrCdtTrf/GrpHdr/SttlmInf/InstgRmbrsmntAgt/FinInstnId/BICFI |
| [AAAAJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaajpjt.md) | InstdRmbrsmntAgt | /FIToFICstmrCdtTrf/GrpHdr/SttlmInf/InstdRmbrsmntAgt/FinInstnId/BICFI |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | InstgAgt | /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | InstdAgt | /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | Dbtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | DbtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | CdtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [DEF Electronics](../../../../../../../shared/reference/participants/participant-src-000162-example-def-electronics-bf4c618.md) | Cdtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14 and wrapped in Document passed the exact supplied XSD src-000169. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table AcceptanceDateTime 2015-09-28T15:45:00; complete XML P1284–P1392 contains no AccptncDtTm.
- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.
- Table tag <Type> is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FIToFICstmrCdtTrf>
	<GrpHdr>
		<MsgId>BBBB/150928-CCT/JPY/123</MsgId>
		<CreDtTm>2015-09-28T16:00:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>COVE</SttlmMtd>
			<InstgRmbrsmntAgt>
				<FinInstnId>
					<BICFI>CCCCJPJT</BICFI>
				</FinInstnId>
			</InstgRmbrsmntAgt>
			<InstdRmbrsmntAgt>
				<FinInstnId>
					<BICFI>AAAAJPJT</BICFI>
				</FinInstnId>
			</InstdRmbrsmntAgt>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>AAAAGB2L</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>BBBB/150928-CCT/JPY/123/1</InstrId>
			<EndToEndId>ABC/4562/2015-09-08</EndToEndId>
			<TxId>BBBB/150928-CCT/JPY/123/1</TxId>
		</PmtId>
		<PmtTpInf>
			<InstrPrty>NORM</InstrPrty>
		</PmtTpInf>
		<IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
		<ChrgBr>SHAR</ChrgBr>
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
		<CdtrAgt>
			<FinInstnId>
				<BICFI>AAAAGB2L</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<Cdtr>
			<Nm>DEF Electronics</Nm>
			<PstlAdr>
				<StrtNm>Mark Lane</StrtNm>
				<BldgNb>55</BldgNb>
				<PstCd>EC3R7NE</PstCd>
				<TwnNm>London</TwnNm>
				<Ctry>GB</Ctry>
				<AdrLine>Corn Exchange 5th Floor</AdrLine>
			</PstlAdr>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<Othr>
					<Id>23683707994215</Id>
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
					<Dt>2015-09-08</Dt>									
					</RltdDt>
				</RfrdDocInf>
			</Strd>
		</RmtInf>
	</CdtTrfTxInf>
</FIToFICstmrCdtTrf>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-08.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
