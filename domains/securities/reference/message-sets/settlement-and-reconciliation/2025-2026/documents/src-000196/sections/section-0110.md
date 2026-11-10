---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionAuditTrailReport semt.022.001.07"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionAuditTrailReport semt.022.001.07

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesSettlementTransactionAuditTrailReport semt.022.001.07.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1552** SecuritiesSettlementTransactionAuditTrailReport semt.022.001.07

**P1553** Description

**P1554** On the 15 January 2019, the account servicer, Dresdner Bank London (DRESGB2L) sends to a third party (for example, a CSD) the status of a specific transaction using the SecuritiesSettlementTrasactionAuditTrailReport (semt.022.001.03). 

**P1555** Business Data

**P1556** Number of page: 1

**P1557** Last Page Indicator: Yes

**P1558** Query Reference: SecTransStatQry1

**P1559** Account Owner Transaction Id: FRTJ123DEL1

**P1560** Safekeeping Account: 222S

**P1561** Account Owner: DRESDEFF

**P1562** Status details: on Jan 14, transaction was pending and on Jan 15, it settled

**P1563** Message Instance

**P1564** <SctiesSttlmTxAudtTrlRpt>

**P1565** 	<Pgntn>

**P1566** 		<PgNb>1</PgNb>

**P1567** 		<LastPgInd>true</LastPgInd>

**P1568** 	</Pgntn>

**P1569** 	<QryRef>

**P1570** 		<Id>SecTransStatQry1</Id>

**P1571** 	</QryRef>

**P1572** 	<TxId>

**P1573** 		<AcctOwnrTxId>FRTJ123DEL1</AcctOwnrTxId>

**P1574** 	</TxId>

**P1575** 	<SfkpgAcct>

**P1576** 		<Id>222S</Id>

**P1577** 	</SfkpgAcct>

**P1578** 	<AcctOwnr>

**P1579** 		<AnyBIC>DRESDEFF</AnyBIC>

**P1580** 	</AcctOwnr>

**P1581** 	<StsTrl>

**P1582** 		<StsDt>2019-01-14T15:00:00</StsDt>

**P1583** 		<SttlmSts>

**P1584** 			<Pdg>

**P1585** 				<Rsn>

**P1586** 					<Cd>

**P1587** 						<Cd>COLL</Cd>

**P1588** 					</Cd>

**P1589** 				</Rsn>

**P1590** 			</Pdg>

**P1591** 		</SttlmSts>

**P1592** 	</StsTrl>

**P1593** 	<StsTrl>

**P1594** 		<StsDt>2019-01-15T15:00:00</StsDt>

**P1595** 		<Sttld>

**P1596** 			<AddtlRsnInf>no further info</AddtlRsnInf>

**P1597** 		</Sttld>

**P1598** 	</StsTrl>

**P1599** </SctiesSttlmTxAudtTrlRpt>

