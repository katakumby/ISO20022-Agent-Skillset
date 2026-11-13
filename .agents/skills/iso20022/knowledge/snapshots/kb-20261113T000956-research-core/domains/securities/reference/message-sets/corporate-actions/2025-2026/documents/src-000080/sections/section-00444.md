---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.5 IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd>"]
file_pages: [598]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.5 IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 598 to 598.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 598

```text
CodeName Name Definition
REFU RefundedSecurityIndicator New security issued that has been
refunded to an earlier maturity date.
Applicable only in the frame of a partial
defeasance PDEF corporate action
event.
NREF NonRefundedSecurityIndicator New Security issued that has not been
refunded and the maturity date of the
original underlying security is
unchanged. Applicable only in the frame
of a Partial Defeasance PDEF corporate
action event.
8.4.12.10.5  IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd>
Presence: [0..1]
Definition: Proceeds are taxable according to the information provided by the issuer / offeror.
IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> contains one of the following
IssuerOfferorTaxabilityIndicator2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 598
Or}   Proprietary <Prtry> [1..1] ± 598
8.4.12.10.5.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify information regarding the issuer / offeror taxability status.
Datatype: "IssuerTaxability2Code" on page 1218
CodeName Name Definition
TXBL Taxable The relevant proceeds are taxable.
8.4.12.10.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification to specify information regarding the issuer / offeror taxability status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
8.4.12.10.6  IncomeType <IncmTp>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 598 February 2026
```

