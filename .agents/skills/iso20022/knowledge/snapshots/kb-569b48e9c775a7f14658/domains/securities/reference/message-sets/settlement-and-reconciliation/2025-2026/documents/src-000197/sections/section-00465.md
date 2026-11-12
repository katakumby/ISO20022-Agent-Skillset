---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "21.4 Message Building Blocks"]
file_pages: [713]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
---

# 21.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 713 to 713.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 713

```text
C23 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C24 SecuritiesMarketPracticeGroupGuideline
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the use of this message.
These market practices are available on www.smpg.info.
This constraint is defined at the MessageDefinition level.
C25 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C26 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
21.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
21.4.1 CancellationRequestReference <CxlReqRef>
Presence: [1..1]
Definition: Reference to the unambiguous identification of the cancellation request as per the account
owner.
Datatype: "Max35Text" on page 2192
21.4.2 TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Impacted by: C13 "NoAccountOwnerTransactionIdentificationRule"
TransactionIdentification <TxId> contains the following elements (see "TransactionIdentifications52"
on page 1515 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1515
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1515
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1515
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1515
   NonceIdentification <NonceId> [0..1] Text 1516
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] ± 1516
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 713 March 2026
```

