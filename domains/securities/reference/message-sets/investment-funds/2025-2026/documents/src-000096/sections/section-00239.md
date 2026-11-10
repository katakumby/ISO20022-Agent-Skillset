---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.21 LocalMarketAnnex <LclMktAnx>", "15.4.5.21.6 CashSettlementDetails <CshSttlmDtls>", "15.4.5.21.6.2 PrimaryAccount <PmryAcct>", "15.4.5.21.6.2.1 AccountIdentification <AcctId>"]
file_pages: [342]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.21.6.2.1 AccountIdentification <AcctId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 342 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
PrimaryAccount <PmryAcct> contains the following CashAccount206 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1]  342
     Identification <Id> [1..1] ± 342
     Name <Nm> [0..1] Text 342
   Servicer <Svcr> [0..1] IdentifierSet C2 342
   AccountTypeDescription <AcctTpDesc> [0..1] Text 343
15.4.5.21.6.2.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
AccountIdentification <AcctId> contains the following AccountIdentificationAndName7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 342
   Name <Nm> [0..1] Text 342
15.4.5.21.6.2.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following elements (see "CashAccountIdentification8Choice" on
page 4339 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Other <Othr> [1..1] ± 4339
Or}   IBAN <IBAN> [1..1] IdentifierSet C19 4340
15.4.5.21.6.2.1.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
15.4.5.21.6.2.2  Servicer <Svcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is, manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 342 May 2026
```

