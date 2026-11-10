---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.5 IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd>", "3.4.11.24.5.2 Proprietary <Prtry>"]
file_pages: [185]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.5.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 185 to 185.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 185

```text
3.4.11.24.5.2  Proprietary <Prtry>
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
3.4.11.24.6  NewSecuritiesIssuanceIndicator <NewSctiesIssncInd>
Presence: [0..1]
Definition: Specifies the nature of the securities issue.
Datatype: "NewSecuritiesIssuanceType5Code" on page 1221
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
3.4.11.24.7  IncomeType <IncmTp>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 185 February 2026
```

