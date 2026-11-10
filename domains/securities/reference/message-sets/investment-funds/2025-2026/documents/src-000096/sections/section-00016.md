---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["2 acmt.001.001.08 AccountOpeningInstructionV08", "2.4 Message Building Blocks", "2.4.14 AdditionalInformation <AddtlInf>"]
file_pages: [36]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08"]
---

# 2.4.14 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 36 to 36.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
ServiceLevelAgreement <SvcLvlAgrmt> contains the following elements (see "DocumentToSend4"
on page 5144 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 5144
   Recipient <Rcpt> [1..1] ± 5145
   MethodOfTransmission <MtdOfTrnsmssn> [1..1]  5145
{Or     Code <Cd> [1..1] CodeSet 5145
Or}     Proprietary <Prtry> [1..1] ± 5145
2.4.14 AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information such as remarks or notes that must be conveyed about the account
management activity and or any limitations and restrictions.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditiononalInformation13"
on page 4867 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Limitation <Lmttn> [0..1] Text 4867
   AdditionalInformation <AddtlInf> [0..1] Text 4867
   AccountValidation <AcctVldtn> [0..1] Text 4868
   Type <Tp> [0..1] Text 4868
   Regulator <Rgltr> [0..1] ± 4868
   Status <Sts> [0..1]  4868
{Or     Code <Cd> [1..1] CodeSet 4868
Or}     Proprietary <Prtry> [1..1] ± 4869
   Period <Prd> [0..1] ± 4869
2.4.15 MarketPracticeVersion <MktPrctcVrsn>
Presence: [0..1]
Definition: Identifies the market practice to which the message conforms.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 36 May 2026
```

