---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.4 Balance", "9.1.4.1 SecuritiesBalanceType6Choice", "9.1.4.1.2 Proprietary <Prtry>"]
file_pages: [199]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.4.1.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 199 to 199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 199

```text
CodeName Name Definition
CLEN TaxExempt Tax-exempt financial instruments are to
be settled.
DIRT NonTaxExempt Taxable financial instruments are to be
settled.
NOMI Registered Balance of financial instruments that are
registered (in nominee name or in the
name of the beneficial owner).
SPOS StreetPosition Balance of financial instruments that
remain registered in the name of the
prior beneficial owner.
UNRG Unregistered Balance of securities that could not be
registered due to foreign ownership
limitation.
ISSU Issued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has been received.
QUAS QuasiIssued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has not yet been
received.
LODE PendingOnLoanDelivery Balance of financial instruments that are
pending delivery in relation to a lending
transaction.
9.1.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Sub-balance expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.4.2  SecuritiesSubBalanceTypeAndQuantityBreakdown3
Definition: Quantity breakdown information for a specific securities balance.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 200
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 200
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 199 September 2025
```

