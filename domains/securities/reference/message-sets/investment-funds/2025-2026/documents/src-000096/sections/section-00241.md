---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.21 LocalMarketAnnex <LclMktAnx>", "15.4.5.21.6 CashSettlementDetails <CshSttlmDtls>", "15.4.5.21.6.3 SecondaryAccount <ScndryAcct>", "15.4.5.21.6.3.1 AccountIdentification <AcctId>", "15.4.5.21.6.3.1.2 Name <Nm>"]
file_pages: [344]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.21.6.3.1.2 Name <Nm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 344 to 344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 344

```text
Identification <Id> contains one of the following elements (see "CashAccountIdentification8Choice" on
page 4339 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Other <Othr> [1..1] ± 4339
Or}   IBAN <IBAN> [1..1] IdentifierSet C19 4340
15.4.5.21.6.3.1.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
15.4.5.21.6.3.2  Servicer <Svcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is, manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
15.4.5.21.6.3.3  AccountTypeDescription <AcctTpDesc>
Presence: [0..1]
Definition: Additional means of identification of the account, as designated by the account servicer in
agreement with the account owner.
Datatype: "Max35Text" on page 5403
15.4.5.21.7  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the fund order desk.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 344 May 2026
```

