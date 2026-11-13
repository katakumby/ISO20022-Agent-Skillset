---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.11 ExecutingPerson <ExctgPrsn>", "22.1.13.2.11.2 Algorithm <Algo>"]
file_pages: [390]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.11.2 Algorithm <Algo>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 390 to 390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 390

```text
Person <Prsn> contains the following elements (see "PersonIdentification12" on page 345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CountryOfBranch <CtryOfBrnch> [1..1] CodeSet C4 346
   Other <Othr> [1..1]  346
     Identification <Id> [1..1] Text 346
     SchemeName <SchmeNm> [0..1]  347
{Or       Code <Cd> [1..1] CodeSet 347
Or}       Proprietary <Prtry> [1..1] Text 347
     Issuer <Issr> [0..1] Text 347
22.1.13.2.11.2  Algorithm <Algo>
Presence: [1..1]
Definition: Identification of an algorithm.
Datatype: "Max50Text" on page 456
22.1.13.2.11.3  Client <Clnt>
Presence: [1..1]
Definition: Indication that the transaction was executed directly by the client.
Datatype: "NoReasonCode" on page 442
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
22.1.13.2.12  AdditionalAttributes <AddtlAttrbts>
Presence: [1..1]
Definition: Provides additional indicators on the reported transaction.
AdditionalAttributes <AddtlAttrbts> contains the following SecuritiesTransactionIndicator2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   WaiverIndicator <WvrInd> [0..*] CodeSet 391
   ShortSellingIndicator <ShrtSellgInd> [0..1] CodeSet 391
   OTCPostTradeIndicator <OTCPstTradInd> [0..*] CodeSet 391
   RiskReducingTransaction <RskRdcgTx> [0..1] Indicator 392
   SecuritiesFinancingTransactionIndicator
<SctiesFincgTxInd>
[1..1] Indicator 392
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
390 July 2025
```

