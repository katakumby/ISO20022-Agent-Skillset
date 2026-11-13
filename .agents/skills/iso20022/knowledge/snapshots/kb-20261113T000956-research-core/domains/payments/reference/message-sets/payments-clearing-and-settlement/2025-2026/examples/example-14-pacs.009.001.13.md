---
template: false
document_kind: "message-example"
title: "FinancialInstitutionCreditTransfer pacs.009.001.13 - 1"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000170"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P2036–P2147; T41", "heading_path": ["Business Examples", "FinancialInstitutionCreditTransfer pacs.009.001.13 - 1", "First FinancialInstitutionCreditTransfer"]}, {"source_id": "src-000170", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-aaaajpjt", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-ccccjpjt", "participant-src-000162-example-def-electronics-46588bb"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# FinancialInstitutionCreditTransfer pacs.009.001.13 - 1

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P2028** FinancialInstitutionCreditTransfer pacs.009.001.13 - 1

**P2029** This example covers two FinancialInstitutionCreditTransfer messages. The first FinancialInstitutionCreditTransfer message is sent by BBBB Bank to CCCC Bank. The second FinancialInstitutionCreditTransfer message is sent by CCCCJPJT to AAAAJPJT.

**P2030** First FinancialInstitutionCreditTransfer

**P2031** Description

**P2032** Under business example 1 of the FIToFICustomerCreditTransfer, BBBB Bank, New York (BBBBUS33) sent an FIToFICustomerCreditTransfer message to AAAA Bank (AAAAGB2L) using the cover method as BBBB Bank does not have a JPY account relationship with AAAA Bank. BBBB Bank uses CCCC Bank, Tokyo as its correspondent. AAAA Bank uses AAAA Bank, Tokyo (AAAAJPJT) as its JPY correspondent.  Immediately after sending the FIToFICustomerCreditTransfer to AAAA Bank, BBBB Bank sends its correspondent CCCC Bank a FinancialInstitutionCreditTransfer message to cover the customer payment.

**P2033** Business Data

**P2034** FinancialInstitutionCreditTransfer from BBBB Bank to CCCC Bank:

**P2035** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0041.md) · [Literal XML payload](../../../../../../../evidence/archived/44c418f547ca62a2d3c049c4.md) · [Source example flow](../flows/example-src-000162-14.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | InstgAgt | /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [CCCCJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccjpjt.md) | InstdAgt | /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | Dbtr | /FICdtTrf/CdtTrfTxInf/Dbtr/FinInstnId/BICFI |
| [AAAAJPJT](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaajpjt.md) | CdtrAgt | /FICdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | Cdtr | /FICdtTrf/CdtTrfTxInf/Cdtr/FinInstnId/BICFI |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | InitgPty | /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/InitgPty/Nm |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | Dbtr | /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/Dbtr/Nm |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | DbtrAgt | /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/DbtrAgt/FinInstnId/BICFI |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | CdtrAgt | /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/CdtrAgt/FinInstnId/BICFI |
| [DEF Electronics](../../../../../../../shared/reference/participants/participant-src-000162-example-def-electronics-46588bb.md) | Cdtr | /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/Cdtr/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13 and wrapped in Document passed the exact supplied XSD src-000170. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table TxId BBBB/150928-CCT/JPY/123/1; XML BBBB/150928-CCT/123/1.
- Table underlying creditor postcode EC3R7NE; XML EC3RZNE.
- Table tag <RfrdDocType> is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.
- Table tag <RfrdDocNb> is retained literally; corresponding instance vocabulary uses Nb. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FICdtTrf>
	<GrpHdr>
		<MsgId>BBBB/150928-FICT/JPY/430</MsgId>
		<CreDtTm>2015-09-28T16:00:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>INDA</SttlmMtd>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>CCCCJPJT</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>BBBB/150928-FICT/JPY/430/1</InstrId>
			<EndToEndId>ABC/4562/2015-09-08</EndToEndId>
			<TxId>BBBB/150928-CCT/123/1</TxId>
		</PmtId>
		<IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
		<Dbtr>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</Dbtr>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>AAAAJPJT</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<Cdtr>
			<FinInstnId>
				<BICFI>AAAAGB2L</BICFI>
			</FinInstnId>
		</Cdtr>
		<UndrlygCstmrCdtTrf>
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
					<PstCd>EC3RZNE</PstCd>
					<TwnNm>London</TwnNm>
					<Ctry>GB</Ctry>
					<AdrLine>Corn Exchange 5th Floor</AdrLine>
				</PstlAdr>
			</Cdtr>
			<CdtrAcct>
				<Id>
					<Othr>
						<Id>29683707994815</Id>
					</Othr>
				</Id>
			</CdtrAcct>
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
		</UndrlygCstmrCdtTrf>
	</CdtTrfTxInf>
</FICdtTrf>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-14.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
