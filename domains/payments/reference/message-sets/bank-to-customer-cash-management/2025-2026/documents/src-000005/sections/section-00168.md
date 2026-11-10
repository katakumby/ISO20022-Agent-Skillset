---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.2 POI <POI>", "2.4.2.15.18.2.26.2.4 Capabilities <Cpblties>", "2.4.2.15.18.2.26.2.4.4 DisplayCapabilities <DispCpblties>"]
file_pages: [244]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.2.4.4 DisplayCapabilities <DispCpblties>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 244 to 244.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 244

```text
2.4.2.15.18.2.26.2.4.4  DisplayCapabilities <DispCpblties>
Presence: [0..*]
Definition: Capabilities of the display components performing the transaction.
DisplayCapabilities <DispCpblties> contains the following DisplayCapabilities1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DisplayType <DispTp> [1..1] CodeSet 244
   NumberOfLines <NbOfLines> [1..1] Text 244
   LineWidth <LineWidth> [1..1] Text 244
2.4.2.15.18.2.26.2.4.4.1  DisplayType <DispTp>
Presence: [1..1]
Definition: Type of display (for example merchant or cardholder).
Datatype: "UserInterface2Code" on page 908
CodeName Name Definition
MDSP MerchantDisplay Merchant display or interface.
CDSP CardholderDisplay Cardholder display or interface.
2.4.2.15.18.2.26.2.4.4.2  NumberOfLines <NbOfLines>
Presence: [1..1]
Definition: Number of lines of the display component.
Datatype: "Max3NumericText" on page 916
2.4.2.15.18.2.26.2.4.4.3  LineWidth <LineWidth>
Presence: [1..1]
Definition: Number of columns of the display component.
Datatype: "Max3NumericText" on page 916
2.4.2.15.18.2.26.2.4.5  PrintLineWidth <PrtLineWidth>
Presence: [0..1]
Definition: Number of columns of the printer component.
Datatype: "Max3NumericText" on page 916
2.4.2.15.18.2.26.2.5  Component <Cmpnt>
Presence: [0..*]
Definition: Data related to a component of the POI performing the transaction.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
244 March 2026
```

