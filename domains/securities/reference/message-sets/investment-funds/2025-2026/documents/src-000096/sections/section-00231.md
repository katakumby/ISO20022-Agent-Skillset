---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.20 CashSettlementDetails <CshSttlmDtls>", "15.4.5.20.2 PrimaryAccount <PmryAcct>", "15.4.5.20.2.3 AccountTypeDescription <AcctTpDesc>"]
file_pages: [333]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.20.2.3 AccountTypeDescription <AcctTpDesc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 333 to 333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 333

```text
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
15.4.5.20.2.3  AccountTypeDescription <AcctTpDesc>
Presence: [0..1]
Definition: Additional means of identification of the account, as designated by the account servicer in
agreement with the account owner.
Datatype: "Max35Text" on page 5403
15.4.5.20.3  SecondaryAccount <ScndryAcct>
Presence: [0..1]
Definition: Sub-division of a master or omnibus cash account.
SecondaryAccount <ScndryAcct> contains the following CashAccount206 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1]  333
     Identification <Id> [1..1] ± 333
     Name <Nm> [0..1] Text 334
   Servicer <Svcr> [0..1] IdentifierSet C2 334
   AccountTypeDescription <AcctTpDesc> [0..1] Text 334
15.4.5.20.3.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
AccountIdentification <AcctId> contains the following AccountIdentificationAndName7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 333
   Name <Nm> [0..1] Text 334
15.4.5.20.3.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 333 May 2026
```

