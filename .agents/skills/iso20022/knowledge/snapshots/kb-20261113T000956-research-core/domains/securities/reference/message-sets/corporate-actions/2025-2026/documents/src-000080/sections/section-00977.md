---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.85 NewSecuritiesIssuanceType5Code"]
file_pages: [1221]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.85 NewSecuritiesIssuanceType5Code

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1221 to 1221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1221

```text
CodeName Name Definition
TXDF TaxDeferred Rate relating to the underlying security
for which tax is deferred.
TXFR TaxFree Rate relating to the underlying security
which is not taxable.
UNFR Unfranked Rate resulting from an unfranked
dividend paid by a company; the rate
does not include tax credit and is subject
to withholding tax.
PAPU PartWayPeriodUnitsIncomePortion Distribution rate relating to the part way
period units, for example Group II units
in UK.
REES RealEstatePropertyIncomePortion Rate of income distribution originated by
real estate investment.
16.2.2.85  NewSecuritiesIssuanceType5Code
Definition: Specifies the type of securities proceeds; whether they are newly issued or not, defeased or
non-defeased.
Type: CodeSet
CodeName Name Definition
DEFE DefeasedSecurityIndicator Funds have been placed in escrow by a
trustee or agent to ensure payment on a
portion of the outstanding balance of the
original security on maturity date.
Applicable only in the frame of a Partial
Defeasance PDEF corporate action
event.
EXIS ExistingIssue Securities proceeds are not new issues.
NEIS NewIssue Securities proceeds are newly issued.
NDEF NonDefeasedSecurityIndicator Funds will not be guaranteed at maturity
by the issuer or paying agent for this
newly issued non-defeased security.
Applicable only in the frame of a Partial
Defeasance PDEF corporate action
event.
UKWN Unknown Not known whether the securities
proceeds are newly issued or not.
NREF NonRefundedSecurityIndicator New Security issued that has not been
refunded and the maturity date of the
original underlying security is
unchanged. Applicable only in the frame
of a Partial Defeasance PDEF corporate
action event.
REFU RefundedSecurityIndicator New security issued that has been
refunded to an earlier maturity date.
Applicable only in the frame of a partial
defeasance PDEF corporate action
event.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1221 February 2026
```

