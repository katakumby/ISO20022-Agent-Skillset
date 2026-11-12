---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesTransactionCancellationRequest sese.020.001.09"]
content_origin: "source-transcription"
---

# SecuritiesTransactionCancellationRequest sese.020.001.09

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / SecuritiesTransactionCancellationRequest sese.020.001.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1600** SecuritiesTransactionCancellationRequest sese.020.001.09

**P1601** Description

**P1602** On the 05 January 2019, Dresdner Bank Frankfurt (DRESDEFF), the account owner, requests from its sub-custodian Dresdner Bank London (DRESGB2L) to cancel a delivery versus payment formerly instructed. This is done through a Securities Transaction Cancellation Request (sese.020.001.05).

**P1603** Business Data

**P1604** Securities Settlement Transaction Id for the DVP: FRTJ123DEL2

**P1605** Securities Movement Type: Delivery

**P1606** Payment: against payment

**P1607** Safekeeping Account: 222S

**P1608** Financial Instrument Identification and description: BE0123456789 Belgium Company

**P1609** XYZ

**P1610** Trade Date: 05/01/2019

**P1611** Settlement Date: 08/01/2019

**P1612** Settlement Quantity: face amount 5,000,000

**P1613** Settlement Amount: EUR 5,057,200 credit

**P1614** Receiving Depository: NBBEBEBB (National Bank of Belgium)

**P1615** Receiving Party 1: CITIBEBB (Citibank)

**P1616** Receiving Party 2: CFPIDEFF (Commerz Financial Products GmbH, Frankfurt), account 321654

**P1617** Message Instance

**P1618** Message Instance

**P1619** <SctiesTxCxlReq>

**P1620** 	<AcctOwnrTxId>

**P1621** 		<SctiesSttlmTxId>

**P1622** 			<TxId>FRTJ123DEL2</TxId>

**P1623** 			<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P1624** 			<Pmt>APMT</Pmt>

**P1625** 		</SctiesSttlmTxId>

**P1626** 	</AcctOwnrTxId>

**P1627** 	<SfkpgAcct>

**P1628** 		<Id>222S</Id>

**P1629** 	</SfkpgAcct>

**P1630** 	<TxDtls>

**P1631** 		<FinInstrmId>

**P1632** 			<ISIN>BE0123456789</ISIN>

**P1633** 			<Desc>Belgium Company XYZ</Desc>

**P1634** 		</FinInstrmId>

**P1635** 		<TradDt>

**P1636** 			<Dt>

**P1637** 				<Dt>2019-01-05</Dt>

**P1638** 			</Dt>

**P1639** 		</TradDt>

**P1640** 		<SttlmDt>

**P1641** 			<Dt>

**P1642** 				<Dt>2019-01-08</Dt>

**P1643** 			</Dt>

**P1644** 		</SttlmDt>

**P1645** 		<SttlmQty>

**P1646** 			<Qty>

**P1647** 				<FaceAmt>5000000</FaceAmt>

**P1648** 			</Qty>

**P1649** 		</SttlmQty>

**P1650** 		<SttlmAmt>

**P1651** 			<Amt Ccy="EUR">5057200</Amt>

**P1652** 			<CdtDbtInd>CRDT</CdtDbtInd>

**P1653** 		</SttlmAmt>

**P1654** 		<RcvgSttlmPties>

**P1655** 			<Dpstry>

**P1656** 				<Id>

**P1657** 					<AnyBIC>NBBEBEBB</AnyBIC>

**P1658** 				</Id>

**P1659** 			</Dpstry>

**P1660** 			<Pty1>

**P1661** 				<Id>

**P1662** 					<AnyBIC>CITIBEBB</AnyBIC>

**P1663** 				</Id>

**P1664** 			</Pty1>

**P1665** 			<Pty2>

**P1666** 				<Id>

**P1667** 					<AnyBIC>CFPIDEFF</AnyBIC>

**P1668** 				</Id>

**P1669** 				<SfkpgAcct>

**P1670** 					<Id>321654</Id>

**P1671** 				</SfkpgAcct>

**P1672** 			</Pty2>

**P1673** 		</RcvgSttlmPties>

**P1674** 	</TxDtls>

**P1675** </SctiesTxCxlReq>

