---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.31 InvestmentPlan17", "66.1.26.31.18 InstalmentManagerRole <InstlmtMgrRole>"]
file_pages: [4799]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.31.18 InstalmentManagerRole <InstlmtMgrRole>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4799 to 4799.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4799

```text
66.1.26.31.18  InstalmentManagerRole <InstlmtMgrRole>
Presence: [0..1]
Definition: Role or function of the instalment manager.
InstalmentManagerRole <InstlmtMgrRole> contains one of the following elements (see
"PartyRole4Choice" on page 4956 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4956
Or}   Proprietary <Prtry> [1..1] ± 4958
66.1.26.32  BenefitCrystallisationEvent2
Definition: Information about the realisation of benefits taken from a pension.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EventTypeNumber <EvtTpNb> [0..1] Text 4799
   EventTypeName <EvtTpNm> [0..1] Text 4799
   EventDate <EvtDt> [0..1] Date 4799
   CrystallisationAmount <CrstllstnAmt> [0..1] Amount C1 4800
   PercentageOfAllowance <PctgOfAllwnc> [0..1] Rate 4800
   LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 4800
   AdditionalInformation <AddtlInf> [0..*] ± 4800
66.1.26.32.1  EventTypeNumber <EvtTpNb>
Presence: [0..1]
Definition: Number of the crystallisation event. In the UK market this could be, for example, BCE5,
BE5A or BCE5B.
Datatype: "Max35Text" on page 5403
66.1.26.32.2  EventTypeName <EvtTpNm>
Presence: [0..1]
Definition: Name of the crystallisation event. In the UK market this could be, for example, 'entitlement to
scheme pension'.
Datatype: "Max35Text" on page 5403
66.1.26.32.3  EventDate <EvtDt>
Presence: [0..1]
Definition: Date on which the crystallisation event was triggered.
Datatype: "ISODate" on page 5388
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4799 May 2026
```

