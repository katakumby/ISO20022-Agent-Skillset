---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["15 camt.016.001.04 GetCurrencyExchangeRateV04", "15.2 Structure"]
file_pages: [506]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.016.001.04"]
---

# 15.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 506 to 506.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 506

```text
15.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <GetCcyXchgRate> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 506
   CurrencyQueryDefinition <CcyQryDef> [0..1]  507
     QueryType <QryTp> [0..1] CodeSet 507
     CurrencyCriteria <CcyCrit> [0..1]  508
{Or       QueryName <QryNm> [1..1] Text 508
Or}       NewCriteria <NewCrit> [1..1]  508
         NewQueryName <NewQryNm> [0..1] Text 508
         SearchCriteria <SchCrit> [1..*]  508
           SourceCurrency <SrcCcy> [1..1] CodeSet C1 509
           TargetCurrency <TrgtCcy> [1..1] CodeSet C1 509
   SupplementaryData <SplmtryData> [0..*] ± C2 509
15.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
15.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
15.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
Approved by the Payments SEG on 04 February 2025 camt.016.001.04 GetCurrencyExchangeRateV04
Cash Management - Maintenance 2024 - 2025 506 February 2025
```

