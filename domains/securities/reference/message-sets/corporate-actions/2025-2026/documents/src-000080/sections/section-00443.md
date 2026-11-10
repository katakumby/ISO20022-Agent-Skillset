---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [597]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 597 to 597.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 597

```text
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
8.4.12.10.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the value is a debit or credit.
Datatype: "CreditDebitCode" on page 1205
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
8.4.12.10.3  TemporaryFinancialInstrumentIndicator <TempFinInstrmInd>
Presence: [0..1]
Definition: Specifies that the security identified is a temporary security identification used for processing
reasons, for example, contra security used in the US.
TemporaryFinancialInstrumentIndicator <TempFinInstrmInd> contains one of the following
elements (see "TemporaryFinancialInstrumentIndicator3Choice" on page 906 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TemporaryIndicator <TempInd> [1..1] Indicator 906
Or}   Proprietary <Prtry> [1..1] ± 906
8.4.12.10.4  NewSecuritiesIssuanceIndicator <NewSctiesIssncInd>
Presence: [0..1]
Definition: Specifies the nature of the securities issue.
Datatype: "NewSecuritiesIssuanceType6Code" on page 1222
CodeName Name Definition
DEFE DefeasedSecurityIndicator Funds have been placed in escrow by a
trustee or agent to ensure payment on a
portion of the outstanding balance of the
original security on maturity date.
Applicable only in the frame of a Partial
Defeasance PDEF corporate action
event.
NDEF NonDefeasedSecurityIndicator Funds will not be guaranteed at maturity
by the issuer or paying agent for this
newly issued non-defeased security.
Applicable only in the frame of a Partial
Defeasance PDEF corporate action
event.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 597 February 2026
```

