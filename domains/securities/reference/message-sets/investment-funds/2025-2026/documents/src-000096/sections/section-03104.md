---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.1 Account", "66.1.1.6 AccountType2Choice"]
file_pages: [4327]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.1.6 AccountType2Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4327 to 4327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4327

```text
66.1.1.6  AccountType2Choice
Definition: Choice of formats for the specification of the type of account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4327
Or}   Proprietary <Prtry> [1..1] ± 4327
66.1.1.6.1  Code <Cd>
Presence: [1..1]
Definition: Type of account expressed as a code.
Datatype: "FundCashAccount4Code" on page 5305
CodeName Name Definition
HEDG HedgeFund Hedge fund account.
CPFO PensionFundOrdinary Central Provident Fund (CPF) ordinary
account.
CPFS PensionFundSpecial Central Provident Fund (CPF) special
account.
SRSA RetirementScheme Supplementary Retirement Scheme
(SRS) account.
CSDO CSDOmnibusAccount Account operated by a CSD in cross-
CSD settlement context.
TOFF TechnicalOffsetAccount Account operated by a CSD in a direct
holding market context.
ICSA InterCSDAccount Account operated by a CSD for
settlement of securities legs for
instructions involving internal CSDs.
CSDM CSDMirrorAccount Account operated by a CSD for mirroring
positions.
CSDP CSDParticipantAccount Account owned by a CSD participant.
PPEN PrivatePensionScheme Private pension account.
CPEN WorkplacePensionSchema Workplace or company pension account.
66.1.1.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of account expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4327 May 2026
```

